import argparse
import os.path as path
import sys
import image_processing.utils.pre_process as pre_process

import cv2 as cv
from omegaconf import OmegaConf

from image_processing.utils.SeesawAlgorithm import SeesawAlgorithm
from image_processing.utils.change_res import change_res_2


def run_algorithm(frame):

    # set video config
    vid_config = OmegaConf.load(f'image_processing/image_processing/utils/config/algorithm/seesaw.yaml')

    # set algorithm config
    alg_config = OmegaConf.load(f'image_processing/image_processing/utils/config/video/crop.yaml')

    # merge config files
    config = OmegaConf.merge(alg_config, vid_config)

    frame = change_res_2(frame, 720)
    frame = pre_process.standardize_frame(frame)
 
    alg = SeesawAlgorithm(config)
    processed_image, angle = alg.process_frame(frame)

    cv.imshow(f'processing', processed_image)
    print(angle)

    return angle

