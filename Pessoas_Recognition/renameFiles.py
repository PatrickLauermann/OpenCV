import urllib
import numpy as np
import cv2
import os
import os

for file_type in ['positivas']:
    for img in os.listdir(file_type):
        os.rename(file_type+"/"+img, file_type + "/"+img.replace(" ", ""))

for file_type in ['negativas']:
    for img in os.listdir(file_type):
        os.rename(file_type+"/"+img, file_type + "/"+img.replace(" ", ""))
