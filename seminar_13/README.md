# _Seminar 13 - Aplicații practice cu concepte de networking_

## Conținut

- chat app folosind sockets
- chat app folosind Django, channels și WebSockets
- port forwarding folosind ngrok

---

**Resurse pentru exemplele prezentate**:

- chat app folosind sockets -> [link aici](https://www.thepythoncode.com/article/make-a-chat-room-application-in-python)
- chat app folosind Django, channels și WebSockets -> [link aici](https://channels.readthedocs.io/en/stable/tutorial/index.html)
- ngrok -> [link aici](https://ngrok.com/)

_WebSockets_ = protocol de comunicare bidirecțională în timp real, care permite comunicarea între un server și un client într-un mod interactiv

- sunt utilizate în special pentru aplicații web și mobile care necesită actualizări frecvente ale datelor sau schimburi rapide de informații între server și client
- protocolul WebSockets este proiectat pentru a înlocui metodele tradiționale de comunicare între server și client, cum ar fi cererile HTTP repetitive
- **caracteristici**:

  - în loc să trimită cereri repetitive la server pentru a obține actualizări, clientul se conectează la server printr-un canal de comunicație WebSocket persistent
  - odată stabilită conexiunea, atât serverul, cât și clientul pot trimite mesaje reciproc fără a mai fi nevoie de trimiterea unei cereri inițiale
  - comunicarea în WebSocket este bidirecțională, ceea ce înseamnă că atât serverul, cât și clientul pot trimite și primi mesaje simultan
  - utilizează un protocol bazat pe TCP și oferă o conexiune persistentă între server și client; acest lucru reduce latenta și overhead-ul asociat cu trimiterea repetată a cererilor HTTP și răspunsurilor și permite actualizări instantanee ale datelor

- majoritatea browserelor moderne și multe framework-uri și biblioteci de dezvoltare web oferă suport pentru WebSockets

**Exemple**:

1. _chat app folosind sockets_
   - în acest exemplu este implementat un chat cli în cadrul căruia clienții conectați sunt diferențiați prin culoarea asociată mesajelor trimise, folosind librăria _colorama_
   - pentru comunicarea bidirecțională server-client, sunt utilizate concepte studiate în seminarele trecute - sockets, multithreading
   - serverul ascultă conexiuni, iar în momentul în care acestea sunt realizate, adaugă informații despre clienții conectați într-o listă
   - totodată, serverul trimite fiecare mesaj primit mai departe către ceilați clienți conectați, simulând o acțiune de tip "broadcast"
   - clientul se conectează la server, așteaptă mesaje de la server (care sunt, de fapt, mesaje primite de la alți clienți și redirecționate de către server) și preia inputul utilizatorului și îl trimite către server
2. _chat app folosind Django, channels și WebSockets_
   - exemplul urmărește realizarea unei aplicații de tip chat, accesibilă prin intermediul unui browser, cu o interfață grafică minimală, în cadrul căreia utilizatorii pot accesa o anumită cameră (room) și trimite și vizualiza toate mesajele trimise în camera respectivă
   - folosind framework-ul Django se inițializează proiectul și chatul
   - sunt create, conform modului de funcționare al framework-ului, view-uri și routing-ul pentru fereastra principală de selectare a unei camere și cea a camerei respective
   - librăria _channels_ este utilizată pentru a trata acțiunile asincron și a permite folosirea WebSockets (în mod tradițional, Django este construit pe modelul de cerere-răspuns, în care serverul primește o cerere HTTP și returnează un răspuns)
   - este scris un consumer care acceptă conexiuni de tip WebSocket la o anumită rută și preia orice mesaj primește, transmițându-l către același WebSocket
   - astfel mesajele sunt trimise către toți clienții conectați la acel WebSocket
3. _port forwarding utilizând **ngrok**_
   - aplicația de tip chat realizată la punctul 2 poate fi expusă pe un URL extern pentru testare prin intermediul conceptului de _port forwarding_
   - în acest sens, traficul de pe portul _8000_, care este cel pe care aplicația rulează, este redirecționat către o adresă externa random alocată de utilitarul ngrok; cât timp procesul este pornit, aplicația este accesibilă la acel URL
