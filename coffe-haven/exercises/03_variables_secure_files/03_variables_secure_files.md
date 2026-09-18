# Variablen und Secure Files

Ziel dieser Übung ist es, Variablen in unsere Pipeline zu integrieren.

## Aufgaben

1. Füge der Pipeline eine Variable `LOG_LEVEL` mit dem Wert `DEBUG` hinzu und verwende diese in mindestens einem Job
2. Lege eine Variable mit demselben Namen `LOG_LEVEL` im GitLab UI unter `Settings → CI/CD → Variables` mit dem Wert `INFO` an
3. Starte die Pipeline per Hand über `Build → Pipelines → New pipeline` und beobachte den Unterschied im Verhalten der Jobs

## Zusatzaufgabe

Ersetze deine Variable `LOG_LEVEL` durch [Inputs](https://docs.gitlab.com/ci/inputs/) und starte erneut eine Pipeline per Hand.

Wie hat sich die Oberfläche verändert?
Wann würdest du welche Methode bevorzugen?

## Hinweise

- Die Projektvariable im GitLab UI muss auf `visible` gesetzt sein, weil der Wert `INFO` zu kurz ist, um als `masked` markiert zu werden. (Siehe [Anforderung an maskierte Variablen](https://docs.gitlab.com/ci/variables/#mask-a-cicd-variable))
