# Complete project details at https://RandomNerdTutorials.co

import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'Housey'
password = 'happynarwhal'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

