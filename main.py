import config as config
from vid_to_frames.convert_to_frames import get_frames


if __name__ == '__main__':
    get_frames(vid_path=config.ROOT_DATA_DIR + '/video_data/test1.mp4')