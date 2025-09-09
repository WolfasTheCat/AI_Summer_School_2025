import time
from pyniryo import *

IP = "169.254.200.200"  # your robot's IP

robot = NiryoRobot(IP)
try:
    # If needed: robot.calibrate_auto()
    mtx, dist = robot.get_camera_intrinsics()  # camera intrinsics

    print("Streaming… press Q or Esc to quit.")
    while True:
        # 1) get frame
        img_raw = uncompress_image(robot.get_img_compressed())
        # 2) undistort using intrinsics
        img = undistort_image(img_raw, mtx, dist)

        # 3) find workspace markers and crop workspace (ratio 1.0 for Vision Set)
        found, markers_vis = debug_markers(img, workspace_ratio=1.0)
        workspace = None
        if found:
            res = extract_img_workspace(img, workspace_ratio=1.0)
            workspace = res[1] if isinstance(res, tuple) else res  # handle both return styles

        # 4) display (30 ms wait; returns last key pressed)
        key = show_img("camera (undistorted)", img, wait_ms=30)
        if workspace is not None:
            show_img("workspace crop", workspace, wait_ms=1)
        else:
            show_img("markers", markers_vis, wait_ms=1)

        if key in (27, ord("q")):
            break

except KeyboardInterrupt:
    pass
finally:
    robot.close_connection()
