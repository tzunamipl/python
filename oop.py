from robot import Robot
from robot import RoboticArm

print("test")
my_robot = Robot("R2D2", 1)
my_robot_2 = Robot("C3PO", "2")
my_robot.say_hi()
my_robot.print_info()
my_robot_2.print_info()

robot_arm = RoboticArm("Bob", 1, 20)
robot_arm.print_info()
robot_arm.pick_object(20, 30)