# Feature Delivery & Auto Deploy

Ziel dieser Übung ist es, eine sichtbare Produkt-Feature-Erweiterung (Promo-Code im Warenkorb) zu integrieren und den CI/CD-Flow so zu erweitern, dass jede Änderung automatisch getestet, gebaut und auf einer Review-Umgebung ausgerollt wird. Ein Merge in den Hauptbranch soll weiterhin automatisch nach Produktion deployen.

## Feature: Promo-Code im Warenkorb

Das Promo-Code-Feature wird im UI sichtbar und funktioniert wie folgt:

- Auf der Warenkorb-Seite erscheint ein Eingabefeld für Promo-Codes.
- Akzeptierte Codes: `WINTER25` (25 % Rabatt) und `WELCOME10` (10 % Rabatt).
- Promo-Codes werden pro Session gespeichert und bleiben nach einem Reload erhalten.
- Im Order Summary wird die Zeile "Promo Discount" mit dem Rabattbetrag angezeigt.
- Bei ungültigen Codes erscheint eine Fehlermeldung, der Betrag bleibt unverändert.

## Aufgaben – Feature Integration

1. Kopiere die Pipeline aus der Musterlösung in deine `.gitlab-ci.yml` und befülle die globalen Variablen mit den Werten, die du in den vorherigen Übungen verwendet hast.
2. Lege einen Branch `feature/promo-code` an. Drücke dafür in deinem Repository auf das `+` Symbol und wähle `New branch` aus. Gib als Branch-Namen `feature/promo-code` ein und erstelle den Branch basierend auf `main`.
3. Öffne die WebIDE und kopiere die Promo-Code-Funktionalität in dein Projekt:
   - Ersetze `app/routes.py` durch die Version in `/exercises/09_feature_release/solution/routes.py` (enthält PROMO_CODES-Dict, POST-Handler, apply_discount-Funktion).
   - Ersetze `app/templates/cart.html` durch die Version in `/exercises/09_feature_release/solution/cart.html` (Promo-Code-Input-Feld und Discount-Anzeige).
   - Ersetze `tests/test_routes.py` mit den Tests aus `/exercises/09_feature_release/solution/test_routes.py` (enthält Promo-Code-Tests).
4. Committe die Änderungen und pushe auf deinen Feature-Branch.

## Abnahme

- Öffne eine Merge-Request vom Branch `feature/promo-code` nach `main`. Gehe dafür in GitLab auf `Merge Requests` → `New Merge Request` → Wähle Source-Branch `feature/promo-code` und Target-Branch `main`. Achte darauf, dass dein Fork als Target-Repository ausgewählt ist.
- Öffne deine deployte Review-Website unter dem Port `8080` und teste den Promo-Code-Flow im UI.
  - Füge ein Produkt zum Warenkorb.
  - Gib einen gültigen Promo-Code ein (z. B. `WINTER25`) und bestätige.
  - Überprüfe, dass der Rabatt berechnet und angezeigt wird.
- Wenn alles funktioniert, kannst du die Merge-Request mergen.

## Hinweise

- Die bereitgestellten Dateien sind produktionsreif. Copy-Paste ist ausreichend.
