from pyniryo import *

IP = "169.254.200.200"      # change if needed
WORKSPACE = "sleep"     # <-- set this to your workspace name from Niryo Studio
SHAPE = ObjectShape.SQUARE  # choose: SQUARE or CIRCLE (or ANY)
COLOR = ObjectColor.RED     # choose: RED, GREEN, BLUE (or ANY)
HEIGHT_OFFSET = 0        # meters above computed pick pose (keep positive & safe)

robot = NiryoRobot(IP)

robot_position = robot.get_pose()

robot_position.metadata.version = 1
robot.set_arm_max_velocity(40)

robot.vision_pick(WORKSPACE, height_offset=HEIGHT_OFFSET, shape=SHAPE, color=COLOR)

robot.move(robot_position)


robot.close_connection()


