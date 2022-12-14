'''
Jahr (3 Bytes = 16.777.216 Möglichkeiten)
Monat (1 Byte = 256 Möglichkeiten)
Tag (1 Byte = 256 Möglichkeiten)
Stunde (1 Byte = 256 Möglichkeiten)
Minute (1 Byte = 256 Möglichkeiten)
Sekunde (1 Byte = 256 Möglichkeiten)

Auf Bit Ebene:
Sekunde und Minute haben jeweils nur 60 Zahlen, heißt: da reichen 2*6 bit aus.
Stunden gibt es 24, da reichen 5 Bit.
Tage gibt es Maximal 31, da reichen auch 5 bit.
Monate gibt es 12, da reichen 4 Bit aus.
Nur Jahre gibt es unbegrenzt, deshalb an der Stelle 3*6 Bits.

(6 + 6 + 5 + 5 + 4 + (6*3)) / 8 = 5,5 bedeutet der ganze Timestamp passt in 6 Bytes anstelle von 8 Bytes.
3 * 6 Bits = 2^(6*3) = 262.144 soviel Jahre ist es dann safe ohne angepasst zu werden.
Die Angabe von Millisekunden ist nicht notwendig, da wir nur auf der Sekundenebene Arbeiten.
'''

import datetime


# Die Aktuelle Uhrzeit wird als Datetime abgerufen
now = datetime.datetime.now()

# Der Datetime Wert wird Formatiert und gesplittet
low = (now.strftime('%Y-%m-%d-%H-%M-%S')).split('-')

# Die Einzelnen Einträge werden abgerufen
y = low.pop(0)
m = low.pop(0)
d = low.pop(0)
h = low.pop(0)
m = low.pop(0)
s = low.pop(0)

# Die Einzelnen Werte werden in Bits umgewandelt
bited_y = "{0:b}".format(int(y))
bited_m = "{0:b}".format(int(m))
bited_d = "{0:b}".format(int(d))
bited_h = "{0:b}".format(int(h))
bited_m = "{0:b}".format(int(m))
bited_s = "{0:b}".format(int(s))

print(bited_y, bited_m, bited_d, bited_h ,bited_m, bited_s)
