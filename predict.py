
import numpy as np
import math
import os

from tensorflow.keras.models import model_from_json
from skimage.measure import compare_ssim as ssim
import cv2
from matplotlib import pyplot as plt
from prepare_images import psnr,mse,compare_images,prepare_images
# define necessary image processing functions

def modcrop(img, scale):
    tmpsz = img.shape
    sz = tmpsz[0:2]
    sz = sz - np.mod(sz, scale)
    img = img[0:sz[0], 1:sz[1]]
    return img


def shave(image, border):
    img = image[border: -border, border: -border]
    return img
# define main prediction function

def predict(image,img_name):
    
    # load the srcnn model with weights
    with open('model.json', "r") as json_file:
            loaded_model_json = json_file.read()
            

    srcnn = model_from_json(loaded_model_json)
    
    srcnn.load_weights('3051crop_weight_200.h5')
    
    # load the degraded and reference images
    #, file = os.path.split(image_path)
    #degraded = cv2.imread(image_path)
    degraded = image
    file=img_name
    ref = cv2.imread('static/input/{}'.format(file))
    
    # preprocess the image with modcrop
    ref = modcrop(ref, 3)
    degraded = modcrop(degraded, 3)
    
    # convert the image to YCrCb - (srcnn trained on Y channel)
    #temp = cv2.cvtColor(degraded, cv2.COLOR_BGR2YCrCb)
    temp = cv2.cvtColor(ref, cv2.COLOR_BGR2YCrCb)
    # create image slice and normalize  
    Y = np.zeros((1, temp.shape[0], temp.shape[1], 1), dtype=float)
    Y[0, :, :, 0] = temp[:, :, 0].astype(float) / 255
    
    # perform super-resolution with srcnn
    pre = srcnn.predict(Y, batch_size=1)
    
    # post-process output
    pre *= 255
    pre[pre[:] > 255] = 255
    pre[pre[:] < 0] = 0
    pre = pre.astype(np.uint8)
    
    # copy Y channel back to image and convert to BGR
    temp = shave(temp, 6)
    temp[:, :, 0] = pre[0, :, :, 0]
    output = cv2.cvtColor(temp, cv2.COLOR_YCrCb2BGR)
    
    # remove border from reference and degraged image
    ref = shave(ref.astype(np.uint8), 6)
    degraded = shave(degraded.astype(np.uint8), 6)
    
    # image quality calculations
    scores = []
    scores.append(compare_images(degraded, ref))
    scores.append(compare_images(output, ref))
    
    # return images and scores
    return ref, degraded, output, scores



