import time
from pyniryo import *

IP = "169.254.200.200"      # change if needed
WORKSPACE = "sleep"     # <-- set this to your workspace name from Niryo Studio
SHAPE = ObjectShape.SQUARE  # choose: SQUARE or CIRCLE (or ANY)
COLOR = ObjectColor.RED     # choose: RED, GREEN, BLUE (or ANY)
HEIGHT_OFFSET = 0.06        # meters above computed pick pose (keep positive & safe)
TRIALS = 5

r = NiryoRobot(IP)
try:
    robot_position = r.get_pose()

    r.set_arm_max_velocity(40)

    for i in range(TRIALS):

        # 3) Ask robot to compute the target pose from camera (built-in pipeline)
        found, target_pose, shape_ret, color_ret = r.get_target_pose_from_cam(
            WORKSPACE, height_offset=HEIGHT_OFFSET, shape=SHAPE, color=COLOR
        )
        if not found:
            print(f"[{i+1}/{TRIALS}] No {SHAPE.name}/{COLOR.name} found.")
            continue

        print(f"[{i+1}/{TRIALS}] Found {shape_ret.name}/{color_ret.name}. "
              f"Moving above it (offset={HEIGHT_OFFSET:.3f} m).")

        target_pose.metadata= PoseMetadata.v1(frame="")
        # 4) Move linearly to the safe-over-object pose
        r.move_to_object("sleep", HEIGHT_OFFSET,SHAPE, COLOR)
        r.wait(0.5)

    # If you prefer, the one-liner alternative is:
    # r.move_to_object(WORKSPACE, height_offset=HEIGHT_OFFSET, shape=SHAPE, color=COLOR)
        r.move(robot_position)

finally:
    r.close_connection()