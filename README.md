# The Open Air Quality Monitor


### Specification / Requirements
The idea for this project is to make an indoor / outdoor air quality monitor that is internet connected and can act as a server for a webapp to access the data.

### Learning Objectives
- ESP32 and IoT (setting up inexpensive microcontroller as internet connected device)
- React webapp for interacting with ESP32

#### Hardware
- Sensors:
  - particulate matter (2.5)
  - CO2
  - VOCs
  - Temp, humidity
- Memory:
  - store a limited amount of data (e.g. a day's worth or so, to account for internet outage).  Not anticipated to need onboard storage (e.g. SD) at this time.
- Connectivity / DataAccess:
  - hardware is internet connected through wifi and can function as a server to be an access point for the measurements
- Interface:
  - Power on/off button
  - Display possibly in the future
- Power:
  - USB-C 5V charger
  - Lipo/LiIon battery
  - Load sharing (unit can operate while being charged)
- Case: TBD, outdoor rated

#### Software




Steps: 
1. install ESPtool (https://github.com/espressif/esptool)
2. Flash esp32 and install micropython firmware 
   1. http://docs.micropython.org/en/latest/esp32/tutorial/intro.html#esp32-intro
   2. (https://micropython.org/download/esp32/)
3. Use Thonny IDE to confirm we have micropython working on ESP32:
   1. https://randomnerdtutorials.com/getting-started-thonny-micropython-python-ide-esp32-esp8266/


Programming Steps / Notes:
1. Because the ESP32 will run `boot.py` and then `main.py` automatically by default, for testing new programs its nice to make a separate program (e.g. `server.py`) and then run it in REPL by using `import server.py` in the REPL CLI.  Note that you need to do a soft reset (`ctrl+D`) to rerun the program (you will get a `no module named `server.py` error otherwise.)


### References


##### ESP32
1. Schematic, pin mapping, etc.: https://docs.zerynth.com/latest/reference/boards/doit_esp32/docs/

1. How to Get the Best from Low-Cost Particulate Matter Sensors: Guidelines and Practical Recommendations https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7309006/
2. https://aws.amazon.com/blogs/compute/building-an-aws-iot-core-device-using-aws-serverless-and-an-esp32/
3. 
