kubectl run curltest \
  --rm -it \
  --image=curlimages/curl \
  --restart=Never \
  -- sh
# Dann folgendes eingeben curl http://containerapp/api/v1/kasse

