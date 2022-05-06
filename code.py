import ujson
import machine
import urequests
import SSD1306
import time
from machine import Pin, I2C


def main():
    while True:
        i2c = machine.I2C(machine.Pin(5), machine.Pin(4))
        oled = SSD1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)
        json = urequests.get("http://192.168.30.194/json")
        meteo = ujson.loads(json.text)
        oled.fill(0)
        oled.show()
        a = "Temperature:" + str(meteo["body"]["meteo"]["temperature"])
        b = "Humidite:" + str(meteo["body"]["meteo"]["humidity"])
        c = "Altitude:" + str(meteo["body"]["meteo"]["altitude"])
        d = "Pression:" + str(meteo["body"]["meteo"]["pressure"])
        oled.text(a, 0, 0)
        oled.text(b, 0, 15)
        oled.text(c, 0, 30)
        oled.text(d, 0, 45)
        oled.show()
        time.sleep(1)


if __name__ == "__main__":
    main()