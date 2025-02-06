class Robot:
    def __init__(self, name, version_number):
        self.name = name
        self.version_number = version_number
        self.internal_temperature = 39.0

    def say_hi(self):
        print("Hello, my name is " + self.name + ", ready to help!")

    def init_hardware(self):
        print("Init...")

    def print_info(self):
        self.say_hi()
        print("Version number: " + str(self.version_number))
        print("TEmperature: " + str(self.internal_temperature))

print("test")
my_robot = Robot("R2D2", 1)
my_robot.say_hi()
my_robot.print_info()