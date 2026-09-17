# Notizen Tag 2

## Resource Quota

## Limit Range

## Volumes
Config Maps können in einem Volume ausgeliefert werden. Damit ist die Config nicht mehr Container sondern Pod abhängig.
Volumes können Pod, Node oder Clusterabhängig sein
Anwendungsfall:
Sidecar Pattern: App-Container mit Volume auf dem Logs geschrieben werden. Sidecar mit "log-exporter"

## Labels
Metainformationen die von Kubernetes verwendet werden

## Annotations
Metainformationen die nicht von Kubernetes verwendet werden

## ReplicaSet
Verwaltet Pods anhand von Labels (n-Pods die label "app.kubernetes.io/name"=MyApp enthalten)

## Services
*TODO* Nacharbeiten!! 