# _Seminar 3_

## Conținut 

- socket server complet python TCP/UDP
- multicast și broadcast
- TCP tunnel
***

**Broadcast** - procesul de a trimite un pachet de la un host către toate hosturile dintr-o rețea.

- un sender, mai mulți receiveri;
- are loc exclusiv în rețeaua locală

**Multicast** - concept al sistemelor distribuite ce ilustrează comunicarea de grup în cadrul unei rețele (one-to-many, many-to-many). În cadrul multicast, pachetele sunt trimise către mașinile care vor să îl primească. Există mai multe tipuri de multicast:

- IP multicast - este folosit protocolul IP pentru trimiterea datelor
- UDP multicast - este folosit protocolul UDP pentru trimiterea datelor

Deși UDP nu este considerat a fi un protocol de încredere, deoarece nu există garanția livrării mesajelor, UDP multicast este rapid, lightweight și alegerea făcută în, spre exemplu, multe scenarii de streaming (Netflix utilizează UDP multicast pentru spectatorii unui anumit serial ori film).

**Tunneling** - redirecționarea traficului de la un port ocupat către un port disponibil; acest proces permite conexiunilor făcute către un port local (pe desktopul curent) să fie transmise către un computer remote printr-un canal securizat.
