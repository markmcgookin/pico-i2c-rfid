import board
import adafruit_st25dv16
import busio

i2c = busio.I2C(board.GP1, board.GP0)
eeprom = adafruit_st25dv16.EEPROM_I2C(i2c)

# Value    Protocol
# -----    --------
# 0x00     No prepending is done ... the entire URI is contained in the URI Field
# 0x01     http://www.
# 0x02     https://www.
# 0x03     http://
# 0x04     https://

#Goal: https://circuitpython.org/
#head=0x04
#str="circuitpython.org/"

#Goal: https://learn.adafruit.com/adafruit-st25dv16k-i2c-rfic-eeprom-breakout
head=0x04
str="markmcgookin.com"

#Goal: https://www.poureva.be/spip.php?article997
#head=0x02
#str="poureva.be/spip.php?article997"


l=len(str)

buf = bytearray ([0xe1, 0x40, 0x40, 0x05, 0x03, 0x00, 0xd1, 0x01, 0x00, 0x55])
buf[5] = (l+5)
buf[8] = (l+1)
eeprom[0:len(buf)]=buf
eeprom[len(buf)]=head
k=len(buf)+1
eeprom[k:k+l]=bytearray(str)
eeprom[k+l]=0xfe

print("length: {}".format(len(eeprom)))

for i in range(0, 5):
    j = i * 16
    hex_string = ":".join("%02x" % b for b in eeprom[j:j+15])
    print(j, "> ", hex_string, "> ", eeprom[j:j+15])

while True:
    pass
