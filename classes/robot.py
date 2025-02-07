import time

def comp_reach(x_1, y_1, x_2, y_2, reach):
    print("Required reach is " + str(max(abs(x_1 - x_2), abs(y_1 - y_2))))
    if (abs(x_1 - x_2) > reach) or (abs(y_1 - y_2) > reach):
        return False
    else:
        return True

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
        print("Pick object at (" + str(x) + ", " + str(y) + ")")

    def place_object(self, x, y):
        print("Place object at (" + str(x) + ", " + str(y) + ")")

class PackagingSolution:
    def __init__(self, robot_right, robot_left):
        self.robot_left = robot_left
        self.robot_right = robot_right

    def package(self, pick_x, pick_y, middle_x, middle_y, place_x, place_y):
        if comp_reach(pick_x, pick_y, middle_x, middle_y, self.robot_right.reach) and comp_reach(place_x, place_y, middle_x, middle_y, self.robot_left.reach):
            self.robot_right.pick_object(pick_x, pick_y)
            self.robot_right.place_object(middle_x, middle_y)
            self.robot_left.pick_object(middle_x, middle_y)
            self.robot_left.place_object(place_x, place_y)
        else:
            time.sleep(2)
            print("Cannot reach!")
