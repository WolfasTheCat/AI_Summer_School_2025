from pyniryo import *
from pyniryo.vision import *

robot = NiryoRobot('169.254.200.200')

robot.calibrate_auto()

# Your code should be here
color_list = [
    [15, 50, 255],
    [255, 0, 0],
    [0, 255, 0],
]

robot.led_ring_alternate(color_list)
robot.led_ring_alternate(color_list, 1, 5, True)
robot.led_ring_alternate(color_list, iterations=10, wait=True)


"""robot.led_ring_flashing([15, 50, 255])
robot.led_ring_flashing([15, 50, 255], 1, 5, True)
robot.led_ring_flashing([15, 25, 155], iterations=5, wait=True)
print("Change color")"""

robot.close_connection()