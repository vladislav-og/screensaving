import numpy as np
from mss import mss
import cv2
import time
import random
import string
import ctypes
# get primary monitor size only for Windows
user32 = ctypes.windll.user32
scr_width = user32.GetSystemMetrics(0)
scr_height = user32.GetSystemMetrics(1)

# create unic absolute path for file
# path = os.path.dirname(os.path.abspath(__file__))
filename = 'video_' + ''.join(random.choice(string.ascii_letters) for m in range(32)) + '.avi'
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
video = cv2.VideoWriter(filename, fourcc, 24, (scr_width, scr_height))
mon = {'top': 40, 'left': 0, 'width': scr_width, 'height': scr_height}
sct = mss()
start_time = time.time()

print("Started recording")
while True:
    sct_img = sct.grab(mon)
    scr_np = np.array(sct_img, dtype='uint8')

    frame = cv2.cvtColor(scr_np, cv2.COLOR_RGB2BGR)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('window', frame)
    video.write(frame)
    print(f"Frame rate is {1 / (time.time() - start_time)} Hz")
    start_time = time.time()
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

video.release()
