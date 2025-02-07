import time

class Robot:
    def __init__(self, name, version_number):
        self.name = name
        self.version_number = version_number
        self.internal_temperature = 39.0

    def say_hi(self):
        print("Hello, my name is " + self.name + ", ready to help!")

    def init_hardware(self):
        print("Initializinag, please wait...")
        time.sleep(0.5)
        print("20%", end="\r")
        time.sleep(1.5)
        print("50%", end="\r")
        time.sleep(2)
        print("90%", end="\r")
        time.sleep(0.5)
        print("95%", end="\r")
        time.sleep(0.25)
        print("100%")
        time.sleep(0.25)
        print("Done!")

    def print_info(self):
        self.init_hardware()
        self.say_hi()
        print("Version number: " + str(self.version_number))
        print("Temperature: " + str(self.internal_temperature))
        print("\n")

class RoboticArm(Robot):
    def __init__(self, name, version_number, reach):
        super().__init__(name, version_number)
        self.reach = reach

    def pick_object(self, x, y):
        self.init_hardware()
        print("Pick object at (" + str(x) + ", " + str(y) + "), robot needs to be at (" + str(x + self.reach) + ", " + str(y) + ").")
