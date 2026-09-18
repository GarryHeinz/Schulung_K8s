# Deployment

Ziel dieser Übung ist es, das bereits gebaute Image aus der Registry auf einen Server zu deployen. Das Deployment erfolgt per SSH und startet den Container via docker run auf dem Zielsystem.

## Aufgaben

Schreibe den Deployment-Job. Folgende Schritte könnten dir dabei helfen:

- Lege folgende Variablen an:
  - `DEPLOY_USER` und `DEPLOY_HOST` für die SSH-Verbindung
  - Registry (`REGISTRY_HOST`, `REGISTRY_PORT`, `REGISTRY_IMAGE_PATH`)
  - das zu deployende Image (`APP_IMAGE`), z.B.:

    ```yaml
    APP_IMAGE: "$REGISTRY_HOST:$REGISTRY_PORT/$REGISTRY_IMAGE_PATH:latest"
    ```

- Lege deinen privaten SSH-Key in den Secure Files ab
- Lade den SSH-Key über Secure Files und richte den SSH-Client ein:
  - GitLab Secure Files installieren (siehe Hinweise)
  - openssh-client installieren (`apk add --no-cache openssh-client`)
  - SSH-Key aus .secure-files/ nach ~/.ssh/ kopieren und Berechtigungen auf `600` setzen
  - ssh-agent starten und Key hinzufügen
  - public key in den `known_hosts` hinterlegen (`ssh-keyscan -H "$DEPLOY_HOST" >> ~/.ssh/known_hosts`)
- Verbinde dich per SSH und starte den Container mit folgenden Schritten:
  - `docker login` um sich bei der Registry einzuloggen (mit --password-stdin + Pipe)
  - `docker pull` um das Image herunterzuladen
  - `docker run` um den Container zu starten

## Zusatzaufgabe

Stoppe und lösche den alten Container, bevor du den neuen deployst

## Hinweise

- Der `DEPLOY_USER` lautet `opc`.
- Nutze deine erhaltene Host-IP für den Deploy-Host
- Folgenden Codeabschnitt kannst du für den Download der Securefiles verwenden:

    ```bash
    apk add --no-cache glab
    glab auth login --job-token $CI_JOB_TOKEN --hostname $CI_SERVER_FQDN --api-protocol $CI_SERVER_PROTOCOL
    glab -R $CI_PROJECT_PATH securefile download --all --output-dir=".secure-files/"
    ```

- Secure Files werden nach dem Download in .secure-files/ abgelegt.
- Achte auf korrekte Dateiberechtigungen:

    | Item            | Sample                   | Numeric       | Bitwise                |
    | --------------- | ------------------------ | ------------- | ---------------------- |
    | SSH folder      | `~/.ssh`                 | 700           | `drwx------`           |
    | Private key     | `~/.ssh/id_rsa`          | 600           | `-rw-------`           |
    | Authorized Keys | `~/.ssh/authorized_keys` | 600           | `-rw-------`           |
    | Config          | `~/.ssh/config`          | 600           | `-rw-------`           |
    | Known Hosts     | `~/.ssh/known_hosts`     | 644           | `-rw-r--r--`           |

- Nutze wo möglich predefined Variables von GitLab. (Siehe [Predefined Variables](https://docs.gitlab.com/ci/variables/predefined_variables/))
