# Building

Ziel dieser Übung ist es, ein Image in der Pipeline zu bauen und in die GitLab Container Registry hochzuladen.

## Aufgaben

1. Implementiere den `build-job` in der Stage `build`
2. Verwende als Image `quay.io/buildah/stable:latest`
3. Lege die Variablen `REGISTRY_HOST`, `REGISTRY_PORT` und `REGISTRY_IMAGE_PATH` an und gefülle sie entsprechend:
   - REGISTRY_HOST: `gitlab-schulung.oci.ordix.de`
   - REGISTRY_PORT: `5050`
   - REGISTRY_IMAGE_PATH: `<dein_gitlab_username>/<projektname>` (z.B. `user1/coffee-haven`)
4. Logge dich in der Registry mit `buildah login` ein. Nutze die Flag `--password-stdin` um das Passwort über eine Pipe zu übergeben (siehe Hinweise für ein Beispiel)
5. Baue das Image mit `buildah bud`
6. Pushe das Image zwei mal in die Registry:
   - Einmal mit dem Tag `latest`
   - Einmal mit dem Tag des aktuellen Commits (`$CI_COMMIT_SHORT_SHA`)

## Hinweise

- Nutze die vordefinierten Umgebungsvariablen CI_REGISTRY_USER und CI_REGISTRY_PASSWORD für den Login.
- Der Imagename wird folgendermaßen aufgebaut:

    ```markdown
    <REGISTRY_HOST>:<REGISTRY_PORT>/<REGISTRY_IMAGE_PATH>:<TAG>
    ```

- Beispiel für den Login mit buildah:

    ```bash
    echo "$CI_REGISTRY_PASSWORD" | buildah login --username "$CI_REGISTRY_USER" --password-stdin "$REGISTRY_HOST:$REGISTRY_PORT"
    ```

- Nutze (wo möglich) predefined Variables von GitLab. (Siehe [Predefined Variables](https://docs.gitlab.com/ci/variables/predefined_variables/))
