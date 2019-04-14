"""Make subdirectories to sepecified dir based on the subdirectories
in another sepecified dir
"""

import os
from os.path import join
import shutil

def folder_is_hidden(p):
    """ Helper function for os.listdir(). 
    Check where a file is a hidden file or not.
    """
    if os.name== 'nt':
        import win32api, win32con
        attribute = win32api.GetFileAttributes(p)
        return attribute & (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
    else:
        return p.startswith('.') #linux-osx

def make_sub_dir(input, output):
    """Make subdirectories to sepecified dir based on the subdirectories in another sepecified dir.

    Args:
        input(string): original image directory. In input, different kinds of vegetations are stored in subdirectories (e.g input/corn/image1.jpg)
        output(string): resized image directory. In output, different kinds of vegetations are stored in subdirectories (e.g output/corn/image1.jpg)
    Returns:
        types(list): names of subdirectory (absolute path) in a list
    """

    # find the names of subdirectory
    types = [f for f in os.listdir(input) if not folder_is_hidden(f)]

    pwd = os.path.dirname(os.getcwd())
    for t in types:
        # create related type folder
        in_path = join(input, t)
        out_path = join(output, t)
        if os.path.exists(out_path):
            shutil.rmtree(out_path)
        os.makedirs(out_path, exist_ok=True)

    return types