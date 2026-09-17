# Tag 3

## Horizontal Pod Autoscaler

## Persistant Volumes

## StatefulSet
-> Deployment mit State
- Deployments sind für zustandslose Anwendungen
- Statefulsets sind für Anwendungen mit inherentem Zustand
- Statefulsets und Services werden über HeadlessServices verwendet
- Deplyoment Volumes: Alle Pods benutzen das gleiche Volume
- StatefulsSet Volumes: Jeder Pod bekommt sein eigenes Volume
- StatefulSets -> Quasi nur für Datenbanken. Redundanzen werden über replicas abgebildet.
  - Datenbankserver hat eigenen Mechanismus für verteilung von Versitiertem Stand. Oder es gibt eine Reade und eine Write Datenbank

## DeamonSets
- Kopie eines Pods auf jedem Node
- Im Windowscontext: Dienst

## Entwicklungsumgebung
- KinD (Kubernetes in Docker)
- miniKube
- k3s (nur linux)
- MicroK8s