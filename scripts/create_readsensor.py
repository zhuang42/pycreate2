#!/usr/bin/env python3

import pycreate2
import time

DESCRIPTION = """
Wakeup the Create 2.
"""




def main():
    port = "/dev/ttyUSB0"
    baud = 115200

    bot = pycreate2.Create2(port=port, baud=baud)

    bot.start()
    bot.power()

    while True:
        try:
            sensor = bot.get_sensors()

            print(sensor.battery_charge, sensor.battery_capacity)

            time.sleep(5)
            
        except KeyboardInterrupt:
            break




if __name__ == "__main__":
    main()
