from classes.robot import Robot, comp_reach
from classes.robot import RoboticArm
from classes.robot import PackagingSolution

robotic_arm_right = RoboticArm("C3PO", 2, 30)
robotic_arm_left = RoboticArm("R2D2", 2, 15)

packaging = PackagingSolution(robotic_arm_right, robotic_arm_left)

packaging.package(10, 5, 45, 20, 30,25)