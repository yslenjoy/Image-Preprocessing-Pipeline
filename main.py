from utils.resize import imagemagick_resize
from utils.io_data_tools import save_as_numpy_file
import os
import argparse
from augmentation import augmentor

def main():
    """Image processing pipeline
    """
    parser = argparse.ArgumentParser()  
    parser.add_argument("-R", "--resize_img", help="resize the image in imgs_de/", action="store_true")
    parser.add_argument("-A", "--augment_img", help="augment the image in imgs_de_resized/", action="store_true")
    args = parser.parse_args()
    
    img_path = os.path.join(os.getcwd(),'imgs_de')
    resize_path = os.path.join(os.getcwd(),'imgs_de_resized')
    augm_path = os.path.join(os.getcwd(),'imgs_de_augment')

    # call imagemagick_resize() when specified in args or no image is resized
    if args.resize_img or os.path.isdir(resize_path) == False:
        os.makedirs('imgs_de_resized', exist_ok=True)
        imagemagick_resize(img_path, resize_path)

    # call imagemagick_resize() when specified in args or no image is resized
    if args.augment_img or os.path.isdir(augm_path) == False:
        os.makedirs('imgs_de_augment', exist_ok=True)
        augmentor(resize_path, augm_path)
    
    # save_as_numpy_file(augm_path, 'imgs_npy_file')
    
if __name__ == '__main__':
    main()
    print("\nDone! :)") 