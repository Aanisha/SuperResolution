
import numpy as np
import math
import os
import ntpath
import cv2
from skimage.measure import compare_ssim as ssim
from matplotlib import pyplot as plt
from keras.models import Sequential
from keras.layers import Conv2D
from keras.optimizers import Adam


# define a function for peak signal-to-noise ratio (PSNR)

def psnr(target, ref):
         
    # assume RGB image
    target_data = target.astype(float)
    ref_data = ref.astype(float)

    diff = ref_data - target_data
    diff = diff.flatten('C')

    rmse = math.sqrt(np.mean(diff ** 2.))

    return 20 * math.log10(255. / rmse)

# define function for mean squared error (MSE)
def mse(target, ref):
    # the MSE between the two images is the sum of the squared difference between the two images
    err = np.sum((target.astype('float') - ref.astype('float')) ** 2)
    err /= float(target.shape[0] * target.shape[1])
    
    return err

# define function that combines all three image quality metrics
def compare_images(target, ref):
    scores = []
    scores.append(psnr(target, ref))
    scores.append(mse(target, ref))
    scores.append(ssim(target, ref, multichannel =True))
    
    return scores

def prepare_images(path, factor):
    
   
    
        
    # open the file
    #img = cv2.imread(path + '/' + file)
    img = cv2.imread(path)
    
    print(ntpath.basename(path))
    # find old and new image dimensions
    h, w, _ = img.shape
    new_height = h // factor
    new_width = w // factor
        
    # resize the image - down
    img = cv2.resize(img, (new_width, new_height), interpolation = cv2.INTER_LINEAR)
        
    # resize the image - up
    img = cv2.resize(img, (w, h), interpolation = cv2.INTER_LINEAR)
        
    # save the image
    print('Saving {}'.format(path))
    #cv2.imwrite('images/{}'.format(ntpath.basename(path)), img)
        
    #path=os.path.join('images/',ntpath.basename(path))

    return img

