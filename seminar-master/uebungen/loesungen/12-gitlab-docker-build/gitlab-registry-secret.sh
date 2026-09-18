# Daten sind anzupassen!
kubectl create secret docker-registry gitlab-registry \
  --docker-server=registry.gitlab.com \
  --docker-username=<meine-Mail-Adresse> \
  --docker-password=<mein-Kennwort> \
  --dry-run=client -o yaml > gitlab-registry-secret.yaml

