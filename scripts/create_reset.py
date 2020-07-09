#!/usr/bin/env python3

import pycreate2
import argparse

DESCRIPTION = """
Resets the Create 2.
"""




def main():
    port = "/dev/ttyUSB0"
    baud = 115200

    bot = pycreate2.Create2(port=port, baud=baud)

    bot.start()
    ret = bot.reset()
    print(ret)

    packet = bot.SCI.read_and_print_all()



if __name__ == "__main__":
    main()
