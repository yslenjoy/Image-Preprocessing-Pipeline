"""Use imagemagick for command line image transformation (resize)
"""

import os
from os.path import join
from utils.make_sub_dir import make_sub_dir, folder_is_hidden

def imagemagick_resize(input, output):
    """Resize images into 224 * 224 using imagemagick,
    resized images are stored in imgs_de_resized/.

    Args:
        input(string): original image directory. In input, different kinds of vegetations are stored in subdirectories (e.g input/corn/image1.jpg)
        output(string): resized image directory. In output, different kinds of vegetations are stored in subdirectories (e.g output/corn/image1.jpg)
    Returns:
        None
    """

    # make new sub sub dir and find the name of sub dir
    types = make_sub_dir(input, output)

    for t in types:
        print('Converting the {} images...'.format(t))
        # create related type folder
        in_path = join(input, t)
        out_path = join(output, t)

        # use imagemagick in command line to resize image into 224 * 224 (to fit a (224, 224, 3) CNN)
        images = [i for i in os.listdir(in_path) if not folder_is_hidden(i)]
        for i in images:
            in_img = join(in_path, i)
            out_img = join(out_path, i)
            os.system('magick {} -resize \'224x224!\' {}'.format(in_img, out_img))
            


