import time
from pyniryo import *

IP = "169.254.200.200"      # change if needed
WORKSPACE = "sleep"     # <-- set this to your workspace name from Niryo Studio
SHAPE = ObjectShape.SQUARE  # choose: SQUARE or CIRCLE (or ANY)
COLOR = ObjectColor.RED     # choose: RED, GREEN, BLUE (or ANY)
HEIGHT_OFFSET = 0        # meters above computed pick pose (keep positive & safe)

robot = NiryoRobot(IP)

id = robot.set_conveyor()
robot.run_conveyor(id,100,ConveyorDirection.FORWARD)
time.sleep(2.5)
robot.stop_conveyor(id)
robot.close_connection()