import cv2

import config
from utils import create_frames_folder


def get_frames(vid_path):
    create_frames_folder()
    my_vid = cv2.VideoCapture(vid_path)

    current_frame = 0

    while True:
        ret, frame = my_vid.read()
        if ret:
            cv2.imwrite(config.FRAMES_DIR + f'/frame{current_frame}.jpg', frame)
            current_frame += 1
        else:
            break