# Short: observe -> grab frame -> crop workspace -> detect red square -> pixels->relative -> move above
import cv2, numpy as np
from pyniryo import NiryoRobot
from pyniryo.vision import uncompress_image, undistort_image, extract_img_workspace, relative_pos_from_pixels

IP, WORKSPACE, HEIGHT_OFFSET = "169.254.200.200", "sleep", 0.06

r = NiryoRobot(IP)
try:
    r.set_arm_max_velocity(40)
    r.set_learning_mode(True); input("Put arm in OBSERVATION pose (4 markers visible), Enter…")
    obs = r.get_pose(); r.set_learning_mode(False); r.move(obs, linear=True)
    mtx, dist = r.get_camera_intrinsics()

    img = uncompress_image(r.get_img_compressed())
    img = undistort_image(img, mtx, dist)
    res = extract_img_workspace(img, workspace_ratio=1.0)
    ws = res[1] if isinstance(res, tuple) else res
    if ws is None: raise RuntimeError("Workspace not found")

    hsv = cv2.cvtColor(ws, cv2.COLOR_BGR2HSV)
    # red mask (two ranges), then clean
    m1 = cv2.inRange(hsv, (0, 90, 80), (10, 255, 255))
    m2 = cv2.inRange(hsv, (170, 90, 80), (180, 255, 255))
    mask = cv2.morphologyEx(m1 | m2, cv2.MORPH_OPEN, np.ones((9,9), np.uint8))

    cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # pick the largest square-like contour
    best = None; area_max = 0
    for c in cnts:
        a = cv2.contourArea(c)
        if a < 400: continue
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02*peri, True)
        if len(approx) == 4:
            w,h = cv2.minAreaRect(c)[1]
            if min(w,h)/max(w,h) > 0.75 and a > area_max:
                best, area_max = c, a
    if best is None: raise RuntimeError("No RED square detected")

    (cx, cy), (w, h), angle_deg = cv2.minAreaRect(best)
    yaw = np.deg2rad(float(angle_deg))
    x_rel, y_rel = relative_pos_from_pixels(ws, int(cx), int(cy))
    target = r.get_target_pose_from_rel(WORKSPACE, x_rel=x_rel, y_rel=y_rel, yaw_rel=yaw, height_offset=HEIGHT_OFFSET)
    r.move(target, linear=True)
finally:
    r.close_connection()
