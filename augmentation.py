"""Image augmentation tools
"""

import Augmentor
import os
from os.path import join
from utils.make_sub_dir import make_sub_dir, folder_is_hidden
from PIL import ImageFile

# To avoid 'OSError: image file is truncated'
ImageFile.LOAD_TRUNCATED_IMAGES = True

def augmentor(input, output,
              flip_prob = 0.2, 
              rotate_prob = 0.6, max_left_rotation = 10, max_right_rotation=10, 
              zoom_prob = 0.4, zoom_min = 1.1, zoom_max = 1.5,
              bright_prob = 0.5, bright_min = 0.75, bright_max = 1.25,
              color_prob = 0.4, color_min = 0.8, color_max = 1.2,
              contrast_prob = 0.5, contrast_min = 0.8, contrast_max = 1.2,
              distort_prob = 0.2, 
              num_of_samples = 200):
    """Augment images using library Augmentor (https://github.com/mdbloice/Augmentor),
    augment images are stored in imgs_de_augment/.

    Augmentation involved: flip, rotation, zoom, brighteness change, saturation change, 
    contrast change, image distortion.
    Default values are set to the augmentation mentioned above, 
    if some of the augmentation is unwanted, set corresponding probability to 0
    (e.g. distort_prob = 0).

    Args:
        input(string): original image directory. 
                       In input, different kinds of vegetations are stored in subdirectories (e.g input/corn/image1.jpg)
        output(string): resized image directory. 
                        In output, different kinds of vegetations are stored in subdirectories (e.g output/corn/image1.jpg)
        (other Augmentor.Pipeline paramters documentation are omiited for now)
        num_of_samples(int): augmentation sample number.
    Returns:
        None
    """

    # make new sub sub dir and find the name of sub dir
    types = make_sub_dir(input, output)
    
    for t in types:
        print('\n---------Augmenting the {} images...'.format(t))
        # create related type folder
        in_path = join(input, t)
        out_path = join(output, t)

        # Create a pipeline
        p = Augmentor.Pipeline(source_directory = in_path, output_directory = out_path)

        if flip_prob:
            # random horizontal or vertical flip images
            p.flip_random(probability = flip_prob)

        if rotate_prob:
            # rotate images with out crop
            p.rotate_without_crop(probability = rotate_prob, max_left_rotation = max_left_rotation, max_right_rotation = max_right_rotation)

        if zoom_prob:
            # zoom images
            p.zoom(probability = zoom_prob, min_factor = zoom_min, max_factor = zoom_max)

        if bright_prob:
            # change images brightness
            p.random_brightness(probability = bright_prob, min_factor = bright_min, max_factor = bright_max)

        if color_prob:
            # change images saturation
            p.random_color(probability = color_prob, min_factor = color_min, max_factor = color_max)

        if contrast_prob:
            # change images saturation
            p.random_contrast(probability = contrast_prob, min_factor = contrast_min, max_factor = contrast_max)

        if distort_prob:
            # images distortion
            p.random_distortion(probability = distort_prob, grid_width = 2, grid_height = 2, magnitude = 2)

        # Sample from the pipeline:
        try:
            p.sample(num_of_samples)
        except OSError:
            print('\n**********Some problems in {}/'.format(t))
            pass

