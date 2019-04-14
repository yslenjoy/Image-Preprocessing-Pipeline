"""
Use imagemagick for command line image transformation (resize)
"""

import os
from os.path import join
import shutil
    
def folder_is_hidden(p):
    """ 
    Helper function for os.listdir(). 
    Check where a file is a hidden file or not.
    """
    if os.name== 'nt':
        import win32api, win32con
        attribute = win32api.GetFileAttributes(p)
        return attribute & (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
    else:
        return p.startswith('.') #linux-osx

def imagemagick_resize(input, output):
    """
    Resize images into 224 * 224 using imagemagick,
    resized images are stored in imgs_de_resized/.

    Args:
        input(string): original image directory. In input, different kinds of vegetations are stored in subdirectories (e.g input/corn/image1.jpg)
        output(string): resized image directory. In output, different kinds of vegetations are stored in subdirectories (e.g output/corn/image1.jpg)
    Returns:
        None
    """

    # find the types of vegetations
    types = [f for f in os.listdir(input) if not folder_is_hidden(f)]
    pwd = os.path.dirname(os.getcwd())
    for t in types:
        print('Converting the {} images...'.format(t))
        # create related type folder
        in_path = join(input, t)
        out_path = join(output, t)
        if os.path.exists(out_path):
            shutil.rmtree(out_path)
        os.makedirs(out_path, exist_ok=True)

        # use imagemagick in command line to resize image into 224 * 224 (to fit a (224, 224, 3) CNN)
        images = [i for i in os.listdir(in_path) if not folder_is_hidden(i)]
        for i in images:
            in_img = join(in_path, i)
            out_img = join(out_path, i)
            os.system('magick {} -resize \'224x224!\' {}'.format(in_img, out_img))
            


