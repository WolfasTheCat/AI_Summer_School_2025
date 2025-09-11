import time
from pyniryo import *

IP = "169.254.200.200"      # change if needed
WORKSPACE = "test2"     # <-- set this to your workspace name from Niryo Studio
WORKSPACE2 = "belt"
SHAPE = ObjectShape.SQUARE  # choose: SQUARE or CIRCLE (or ANY)
COLOR = ObjectColor.GREEN     # choose: RED, GREEN, BLUE (or ANY)
HEIGHT_OFFSET_WORKSPACE = -0.005        # meters above computed pick pose (keep positive & safe)
HEIGHT_OFFSET_WHITE = 0

robot = NiryoRobot(IP)
robot.calibrate_auto()
workspace_1 = JointsPosition(-1.567,0.171,-0.690,-0.034,-1.272,-0.382)
workspace_2 = JointsPosition(0.681,0.004,-0.316,0.026,-1.548,-0.405)
board_1 = JointsPosition(-2.204,-0.922,0.219,0.112,-0.942,-0.379)

robot.move(workspace_1)

robot.vision_pick(WORKSPACE, height_offset=HEIGHT_OFFSET_WORKSPACE, shape=SHAPE, color=COLOR)


robot.move_to_home_pose()
robot.open_gripper()

id = robot.set_conveyor()
robot.run_conveyor(id,100,ConveyorDirection.FORWARD)
while robot.digital_read(PinID.DI5) == PinState.HIGH:
    pass
robot.stop_conveyor(id)
robot.move(workspace_2)
robot.vision_pick(WORKSPACE2, height_offset=HEIGHT_OFFSET_WORKSPACE, shape=SHAPE, color=COLOR)

robot.move(workspace_1)
robot.move(board_1)
robot.open_gripper()
robot. move(workspace_1)

robot.close_connection()