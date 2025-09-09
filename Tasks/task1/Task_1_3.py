import time

from pyniryo import *
from pyniryo.vision import *

robot = NiryoRobot('169.254.200.200')

robot.calibrate_auto()

try:
    robot.set_learning_mode(True)  # free-move by hand
    print("Reading pose... (Ctrl+C to stop)")
    while True:
        p = robot.get_pose()
        print(f"x={p.x:.3f} y={p.y:.3f} z={p.z:.3f}  "
              f"roll={p.roll:.3f} pitch={p.pitch:.3f} yaw={p.yaw:.3f}")
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    robot.close_connection()
