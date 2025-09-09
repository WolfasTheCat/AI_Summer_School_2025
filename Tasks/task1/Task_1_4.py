import time

from pyniryo import *
from pyniryo.vision import *

robot = NiryoRobot('169.254.200.200')

robot.calibrate_auto()

try:
    robot.wait(5)
    robot.move_to_home_pose()
except KeyboardInterrupt:
    pass
finally:
    robot.close_connection()
