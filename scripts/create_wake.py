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

    while True:
        try:
            print("waking")

            bot.wake()
            
            packet = bot.SCI.read_all()
            if packet:
                print(packet)
            
            
        except KeyboardInterrupt:
            bot.power()
            print("Stoping")
            break




if __name__ == "__main__":
    main()
