import os

import config


def create_frames_folder():
    if os.path.isdir(config.FRAMES_DIR):
        pass
    else:
        os.mkdir(config.FRAMES_DIR)