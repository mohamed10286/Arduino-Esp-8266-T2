import WLAN
import STA_IF
import AP_IF
import gc
from ssid_info import SSID, PASSWORD
mywifi = WLAN(STA_IF)
mywifi.active(False)
mywifi.active(True)
ap = WLAN(AP_IF)
ap.active(False)
mywifi.connect(SSID, PASSWORD)
while not mywifi.isconnected():
    pass
print()
print("connecté" + mywifi.config('essid') +
      "adresse IP: " + mywifi.ifconfig()[0])
gc.collect()
