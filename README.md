# Django_python


### Kleines Frage-Antwort-Forum ###

Entwirf ein Datenmodell für folgende Anforderungen:  
  * eine Frage bestehend aus einem Fließtext kann eingestellt werden  
  * es können Antworten im Fließtext auf eine Frage geben werden  
  * eine der Antworten auf eine Frage kann als akzeptiert markiert werden  
  * es soll feststellbar sein, ob eine Frage mit einer akzeptierten Antwort beantwortet ist oder nicht. Zudem soll feststellbar sein, ob eine Antwort die akzeptierte Antwort ist.    
  * es soll eine Liste aller Fragen ausgegeben werden können, die keine akzeptierten Antworten haben (optional: die gar keine Antworten haben)  
  * Entwirf eine view-Funktion zur Anzeige einer Frage, die ein Template ausgibt, in dem die Frage und darunter die Antworten gelistet sind. Am Anfang des Templates sollen die CSS-Regeln definiert werden. Erreichbar ist diese Seite unter der URL /frage/<ID>/  
  * Es werden keine User verwendet, es passiert alles anonym.  
  * Max. Länge eines Textes sind jeweils 1000 Zeichen.  
