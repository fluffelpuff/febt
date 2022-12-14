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
