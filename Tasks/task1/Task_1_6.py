# Hardcoded version: read joints, nudge one joint, then draw a small square in joint space.
import time
from pyniryo import NiryoRobot, JointsPosition

IP = "169.254.200.200"  # change if needed
r = NiryoRobot(IP)
try:
    r.set_arm_max_velocity(40)     # 40% speed
    r.set_learning_mode(False)     # engage motors

    # 1) Read & print current joints (rad)
    j = list(r.get_joints())
    print("Current joints (rad):", [round(x, 3) for x in j])

    # 2) Nudge joint 0 by +0.2 rad using JointsPosition
    j2 = j[:]
    j2[0] += 0.2
    r.move(JointsPosition(*j2))
    time.sleep(0.5)

    # 3) Draw a "square" in joint space by pure add/sub on joints 0 & 1
    base = list(r.get_joints())
    i0, i1 = 0, 1
    dx, dy = 0.10, 0.10  # keep small

    for _ in range(3):  # trace square 3 times
        base[i0] += dx; r.move(JointsPosition(*base)); time.sleep(0.3)  # right
        base[i1] += dy; r.move(JointsPosition(*base)); time.sleep(0.3)  # up
        base[i0] -= dx; r.move(JointsPosition(*base)); time.sleep(0.3)  # left
        base[i1] -= dy; r.move(JointsPosition(*base)); time.sleep(0.3)  # down
finally:
    r.close_connection()
