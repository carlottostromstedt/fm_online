# Yugioh Fusion-Friend

## Beschreibung der Funktionalität
Die Flask-Applikation ist ein einfaches Webanwendung, die es Benutzern ermöglicht, sich zu registrieren und anzumelden. 

Nach der Anmeldung kann der User ein Bild hochladen. Dieses Bild wird mit Image-Recognition analysiert um die Karten in der Hand zu erkennen. Mit den erkannten Karten wird eine Datenbankabfrage gemacht um die möglichen Fusionen zu erhalten. 

Schlussendlich wird dem User auf einer Show-Page eines Boards der analysierte Spielstand gezeigt und die möglichen Fusionen die angewendet werden könnnen.

## Prozess des Projekts

Zuerst habe ich den Python-Code geschrieben für die Image-Recognition.

Nachher habe ich die Webapplikation erstellt.   

### Gelernetes

Mit diesem Projekt habe ich gelerent, wie ich eine 3-Layer-Architektur in einer Webapplikation umsetzen kann und wie man Cookies und Session Handling einsetzt. Ich bin sehr zufrieden mit meinem Ergebnis

## Testcases

| Test                               | Erwartet                                                                  | Resultat                                                                  | Erfolgreich? |
|------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|--------------|
| Registrierung eines neuen Users    | Registrierung Erfolgreich und User an Login-Page weitergeleitet           | Registrierung Erfolgreich und User an Login-Page weitergeleitet           | x            |
| Login für einen registrierten User | User wird eingeloggt und auf die Root-Page weitergeleitet                 | User wird eingeloggt und auf die Root-Page weitergeleitet                 | x            |
| Upload eines Screenshots           | User kann ein Bild hochladen und es wird ein Board erstellt               | User konnte ein Bild hochladen und es wird ein Board erstellt             | x            |
| Fusionen werden angezeigt          | Bild wurde richtig analysiert und die möglichen Fusionen werden angezeigt | Bild wurde richtig analysiert und die möglichen Fusionen werden angezeigt | x            |