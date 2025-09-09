import os
import time
from datetime import datetime
import cv2
from pyniryo import NiryoRobot, PoseObject
from pyniryo.vision import uncompress_image  # per docs

IP = "169.254.200.200"   # change if needed
OUT_DIR = "captures"
NUM_SHOTS = 5            # how many pictures to save

os.makedirs(OUT_DIR, exist_ok=True)

robot = NiryoRobot(IP)
try:
    robot.set_arm_max_velocity(40)   # safer/slower
    robot.set_learning_mode(True)
    input("Move the arm by hand until ALL 4 markers are visible, then press Enter...")
    observation_pose = robot.get_pose()
    print("Recorded observation Pose:", observation_pose.to_list())

    robot.set_learning_mode(False)
    # Ensure we’re exactly at the recorded vantage point
    robot.move(observation_pose)
    robot.wait(0.3)

    for i in range(NUM_SHOTS):
        # Optional pause so you can rearrange objects between captures
        _ = input(f"[{i+1}/{NUM_SHOTS}] Arrange objects, then press Enter to capture (or type 'q' + Enter to quit): ")
        if _.strip().lower() == "q":
            break

        # Grab → uncompress → save
        img_compressed = robot.get_img_compressed()
        img = uncompress_image(img_compressed)  # returns a NumPy array usable with OpenCV

        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        fname = os.path.join(OUT_DIR, f"workspace_{ts}_{i+1}.png")
        cv2.imwrite(fname, img)
        print("Saved:", fname)

        time.sleep(0.2)

finally:
    robot.close_connection()
