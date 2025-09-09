import time
from pyniryo import NiryoRobot, PoseObject, PoseMetadata



robot = NiryoRobot("169.254.200.200")  # change if needed
robot.calibrate_auto()

try:
    robot.set_arm_max_velocity(40)      # 40% as recommended
    robot.set_learning_mode(True)

    a = PoseObject(0.036, -0.189, 0.353, 0.023, 0.195, -1.384, metadata=PoseMetadata.v1(frame=""))
    b = PoseObject(0.134, -0.000, 0.165,0.003, 1.001 ,-0.001, metadata=PoseMetadata.v1(frame=""))
    robot.move(a)
    robot.move(b)


finally:
    robot.move_to_home_pose()
    robot.close_connection()
