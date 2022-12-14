```
Jahr = 3 Bytes
Monat = 1 Byte
Tag = 1 Byte
Stunde = 1 Byte
Minute = 1 Byte
Sekunde = 1 Byte

Auf Bit Ebene:
Sekunde und Minute haben jeweils nur 60 Zahlen, heißt: da reichen 2*6 bit aus.
Stunden gibt es 24, da reichen 5 Bit.
Tage gibt es Maximal 31, da reichen auch 5 bit.
Monate gibt es 12, da reichen 4 Bit aus.
Nur Jahre gibt es unbegrenzt, deshalb an der Stelle 3*6 Bits.

(6 + 6 + 5 + 5 + 4 + (6*3)) "44 bits" / 8 = 5,5 bedeutet der ganze Timestamp passt in 6 Bytes anstelle von 8 Bytes.
3 * 6 Bits = 2^(6*3) = 262.144 soviel Jahre ist es dann safe ohne angepasst zu werden.
Die Angabe von Millisekunden ist nicht notwendig, da wir nur auf der Sekundenebene Arbeiten.
```