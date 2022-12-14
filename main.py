'''
Jahr (3 Bytes = 16.777.216 Möglichkeiten)
Monat (1 Byte = 256 Möglichkeiten)
Tag (1 Byte = 256 Möglichkeiten)
Stunde (1 Byte = 256 Möglichkeiten)
Minute (1 Byte = 256 Möglichkeiten)
Sekunde (1 Byte = 256 Möglichkeiten)

Auf Bit ebene:
Sekunde und Minute haben jeweils nut 60 Zahlen, heißt: da reichen 2*6 bit aus.
Stunden gibt es 24, da reichen 5 Bit.
Tage gibt es Maximal 31, da reichen auch 5 bit.
Monate gibt es 12, da reichen 4 Bit aus.
Nur Jahre gibt es unbegrenzt deshalb an der stelle 3*6 Bits.

(6 + 6 + 5 + 5 + 4 + (6*3)) / 8 = 5,5 bedeutet der ganze Timestamp passt in 6 Bytes anstelle von 8 Bytes. 😎
3 * 6 Bits = 2^(6*3) = 262.144 soviel Jahre ist es dann safe ohne angepasst zu werden.
'''