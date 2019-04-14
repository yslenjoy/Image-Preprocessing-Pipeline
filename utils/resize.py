"""
Use imagemagick for command line image transformation (resize)
"""

import os
from os.path import join
import shutil
    
def folder_is_hidden(p):
    # find whether the file is hidden
    if os.name== 'nt':
        import win32api, win32con
        attribute = win32api.GetFileAttributes(p)
        return attribute & (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
    else:
        return p.startswith('.') #linux-osx

def imagemagick_resize(input, output):
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
            


