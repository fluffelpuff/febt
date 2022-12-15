import datetime

# Erzeugt einen Byted Timestamp
def get_current_timestamp():
    # Die Aktuelle Uhrzeit wird als Datetime abgerufen
    now = datetime.datetime.now()

    # Der Datetime Wert wird Formatiert und gesplittet
    low = (now.strftime('%Y-%m-%d-%H-%M-%S')).split('-')

    # Die Einzelnen Werte werden in Bits umgewandelt
    bited_year = "{0:b}".format(int(low.pop(0))).zfill(6*3)
    bited_month = "{0:b}".format(int(low.pop(0))).zfill(4)
    bited_day = "{0:b}".format(int(low.pop(0))).zfill(5)
    bited_hour = "{0:b}".format(int(low.pop(0))).zfill(5)
    bited_minute = "{0:b}".format(int(low.pop(0))).zfill(6)
    bited_second = "{0:b}".format(int(low.pop(0))).zfill(6)

    # Die Bitwerte werden aufbereitet
    total_bit_string = "".join([bited_year, bited_month, bited_day, bited_hour, bited_minute, bited_second]).zfill(48)
    splited_total_string = [total_bit_string[i:i+8] for i in range(0, len(total_bit_string), 8)]
    inted_value = [int(i, 2) for i in splited_total_string]
    byted_value = bytes(inted_value)
    return byted_value.hex()



current_timestamp = get_current_timestamp()
print(current_timestamp)