from pyniryo import *

from code_examples.connecting_to_robot import robot

IP = "169.254.200.200"      # change if needed
WORKSPACE = "sleep"     # <-- set this to your workspace name from Niryo Studio
SHAPE = ObjectShape.SQUARE  # choose: SQUARE or CIRCLE (or ANY)
COLOR = ObjectColor.RED     # choose: RED, GREEN, BLUE (or ANY)
HEIGHT_OFFSET = 0.06        # meters above computed pick pose (keep positive & safe)

robot = NiryoRobot(IP)
position = robot.get_pose()

try:
    robot.set_arm_max_velocity(40)
    robot.open_gripper()
    input("Press Enter to continue...")
    robot.close_gripper()
    input("Press Enter to continue...")
    robot.open_gripper()
finally:
    robot.move(position)
    robot.close_gripper()
    robot.close_connection()



