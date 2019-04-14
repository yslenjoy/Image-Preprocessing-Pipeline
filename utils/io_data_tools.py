"""Input and output helpers to load and preprocess images.
"""

import cv2
from utils.make_sub_dir import folder_is_hidden
import os
from os.path import join
import numpy as np

def load_and_grayscale(root, path):
    # Load image.
    img = cv2.imread(join(root, path))
    # Convert to grayscale.
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) 
    return img

def load_and_normalize(root, path):
    # Load image.
    img = cv2.imread(join(root, path))
    # Convert to double and normalize.
    img = cv2.normalize(img.astype('float'), None, 
                            0.0, 1.0, cv2.NORM_MINMAX)   
    return img

def save_as_numpy_file(img_dir, out_dir):
    """Save all the images in img_dir into a numpy array 
    with shape (n, 224, 224, 3) by vegetation types. 
    n is number of images in img_dir.

    Args:
        img_dir(string): original image directory. In img_dir, different kinds of vegetations are stored in subdirectories (e.g img_dir/corn/image1.jpg)
        output(string): the directory where .npy file will be saved.
    Returns:
        None
    """

    # find the names of subdirectory
    types = [f for f in os.listdir(img_dir) if not folder_is_hidden(f)]

    for t in types:
        in_path = join(img_dir, t)
        out_path = join(out_dir, t)
        images = [i for i in os.listdir(in_path) if not folder_is_hidden(i)]
        output = np.zeros((len(images), 224, 224, 3))
        for j in range(len(images)):
            output[j] = load_and_normalize(in_path, images[j])
        np.save('{}_np_file'.format(out_path), output)
        break

