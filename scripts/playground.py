# ----------------------------------------------------------------------------
# MIT License
# shows how to get sensor data from the create 2

from pycreate2 import Create2
import time


if __name__ == "__main__":
    port = '/dev/ttyUSB0'
    baud = {
        'default': 115200,
        'alt': 19200  # shouldn't need this unless you accidentally set it to this
    }

    bot = Create2(port=port, baud=baud['default'])
    bot.wake()

    print("Initing")
    packet = bot.SCI.read_and_print_all()


    print("Stopping")
    bot.stop()
    packet = bot.SCI.read_and_print_all()


    print("Starting")
    bot.start()
    packet = bot.SCI.read_and_print_all()

        
    print("Fulling")
    bot.full()
    packet = bot.SCI.read_and_print_all()


    while True:
        try:
            packet = bot.SCI.read_and_print_all()

            sensor = bot.get_sensors()

            print(sensor.open_interface_mode, sensor.battery_charge, sensor.battery_capacity)


            time.sleep(2)
        except KeyboardInterrupt:
            bot.power()
            print("Stoping")
            bot.stop()
            break
    
    