import time
from pyniryo import *

IP = "169.254.200.200"      # change if needed
WORKSPACE = "test2"     # <-- set this to your workspace name from Niryo Studio
SHAPE = ObjectShape.SQUARE  # choose: SQUARE or CIRCLE (or ANY)
COLOR = ObjectColor.RED     # choose: RED, GREEN, BLUE (or ANY)
HEIGHT_OFFSET = -0.005        # meters above computed pick pose (keep positive & safe)

robot = NiryoRobot(IP)
robot.calibrate_auto()
default_pos = JointsPosition(-1.567,0.171,-0.690,-0.034,-1.272,-0.382)
robot.move(default_pos)

robot.vision_pick(WORKSPACE, height_offset=HEIGHT_OFFSET, shape=SHAPE, color=COLOR)


robot.move_to_home_pose()
robot.open_gripper()

id = robot.set_conveyor()
robot.run_conveyor(id,100,ConveyorDirection.FORWARD)
while robot.digital_read(PinID.DI5) == PinState.HIGH:
    pass
robot.stop_conveyor(id)
robot.close_connection()