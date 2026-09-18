# ToDos: Continuous Deployment mit GitLab Container Registry und Kubernetes

Der Branch `cicd-k8s-gitlab` zeigt eine Continuous-Deployment-Pipeline fuer die ToDos-Anwendung. Maven prueft und paketiert die Anwendung, Buildah erstellt daraus ein GitLab-Container-Registry-Image, und Kubernetes rollt genau den unveraenderlichen SHA-Tag in `dev-namespace` aus.

## Pipeline

| Stufe | Job | Aufgabe |
| --- | --- | --- |
| `verify` | `verify:maven` | Fuehrt mit `mvn clean verify` Unit- und Integrationstests aus und speichert `target/todos.jar` als Pipeline-Artefakt. |
| `image` | `build:image` | Baut fuer Merge Requests und Branch-Pipelines ein lokales Image aus dem getesteten JAR. Es publiziert nichts. |
| `image` | `publish:image` | Baut fuer einen geschuetzten direkten Push das Image aus dem Artefakt und publiziert `$CI_COMMIT_SHA` und `latest` in die GitLab Container Registry. |
| `deploy` | `deploy:kubernetes` | Aktualisiert `gitlab-registry-secret`, injiziert den SHA-Tag in `.k8s/deploy_all.yaml`, wendet das Manifest in `dev-namespace` an und wartet auf den Rollout. Bei Fehler wird automatisch ein Rollback ausgefuehrt. |

Merge-Request-Pipelines fuehren nur Maven-Validierung und den lokalen Image-Build aus. Sie publizieren keine Images und fuehren kein Deployment aus. Die Jobs `publish:image` und `deploy:kubernetes` laufen ausschliesslich bei einem direkten Push auf den geschuetzten Branch `cicd-k8s-gitlab`.

Der [Dockerfile](Dockerfile) kopiert ausschliesslich `target/todos.jar` in das Runtime-Image. Er enthaelt keinen Maven-Build; ausgeliefert wird deshalb genau das zuvor getestete CI-Artefakt. Der SHA-Tag ist die unveraenderliche Deployment-Referenz. `latest` wird nur durch geschuetzte Direct-Push-Pipelines aktualisiert.

## GitLab Registry und Kubernetes

Das Image-Ziel wird ausschliesslich aus GitLabs Registry-Variablen gebildet:

```text
$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
```

Falls GitLab `CI_SERVER_TLS_CA_FILE` bereitstellt, installiert der Container-Job die CA fuer `$CI_REGISTRY` im Buildah-Truststore. Maven installiert die Nexus-CA in den Java-Truststore. Die TLS-Pruefung bleibt in beiden Faellen aktiviert.

[.k8s/deploy_all.yaml](.k8s/deploy_all.yaml) enthaelt das vollstaendige Standard-Deployment dieses Szenarios: Deployment und ClusterIP-Service `todos-gitlab`, eine Replik, Actuator-Readiness- und Liveness-Probes auf `/actuator/health`, Requests von `250m` CPU und `512Mi` RAM sowie Limits von `500m` CPU und `1Gi` RAM. Das Deployment verwendet `gitlab-registry-secret` als `imagePullSecret`; es gibt keinen Ingress.

Der Deploy-Job reconciliiert `gitlab-registry-secret` vor dem Apply aus langlebigen, geschuetzten Pull-Zugangsdaten. Er verwendet absichtlich nicht `CI_REGISTRY_PASSWORD`, weil dieses CI-Job-Token nach Ende des Jobs nicht fuer einen dauerhaften Kubernetes-Image-Pull geeignet ist.

## Erforderliche GitLab-Variablen

Die folgenden Variablen muessen als geschuetzte und maskierte CI/CD-Instanzvariablen hinterlegt sein. Zertifikate, Zugangsdaten und Kubernetes-Konfiguration gehoeren nicht in das Repository.

| Variable | Zweck |
| --- | --- |
| `NEXUS_CA_CERT_BASE64` | Base64-kodiertes PEM-Zertifikat der privaten CA fuer Nexus. |
| `NEXUS_MAVEN_URL` | HTTPS-URL des Nexus Maven Public Repositorys fuer die Abhaengigkeitsaufloesung. |
| `NEXUS_USERNAME` | Benutzername mit Leserechten fuer Nexus. |
| `NEXUS_PASSWORD` | Passwort oder Token fuer `NEXUS_USERNAME`. |
| `CI_REGISTRY`, `CI_REGISTRY_IMAGE`, `CI_REGISTRY_USER`, `CI_REGISTRY_PASSWORD` | Von GitLab bereitgestellte Registry-Variablen fuer Image-Veröffentlichung und Zielpfad. |
| `CI_SERVER_TLS_CA_FILE` | Optionale GitLab-Datei-Variable mit der privaten CA fuer die GitLab Container Registry. |
| `GITLAB_REGISTRY_PULL_USERNAME` | Langlebiger Registry-Benutzer mit Pull-Recht fuer das von Kubernetes verwendete Image. |
| `GITLAB_REGISTRY_PULL_PASSWORD` | Passwort oder Token fuer `GITLAB_REGISTRY_PULL_USERNAME`. |

Der GitLab Runner braucht Netzwerkzugriff auf Nexus, die GitLab Container Registry und den Kubernetes-API-Server, Buildah-Faehigkeit und den Runner-Tag `kubernetes`. Der Deploy-Job verwendet den aktuellen Kontext der eingebundenen Kubeconfig und arbeitet ausschliesslich im expliziten Namespace `dev-namespace`.

## Lokale Entwicklung

```bash
./mvnw clean verify
docker build --tag todos:local .
```

Der Docker-Build setzt das zuvor von Maven erzeugte `target/todos.jar` voraus. Lokales Pushen und Deployen sind nicht Bestandteil dieses Szenarios.