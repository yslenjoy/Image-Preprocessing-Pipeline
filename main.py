from utils.resize import imagemagick_resize
from utils.io_data_tools import save_as_numpy_file
import os
import argparse
from augmentation import augmentor
from display_map import get_same_type_coordinates

def main():
    """Image processing pipeline
    """
    parser = argparse.ArgumentParser()  
    parser.add_argument("-R", "--resize_img", help="resize images from imgs_de/", action="store_true")
    parser.add_argument("-A", "--augment_img", help="augment images from imgs_de_resized/", action="store_true")
    parser.add_argument("-S", "--save_np_file", help="save the normalized np file from cv2.imread", action="store_true")
    parser.add_argument("-P", "--plot_geo_info", help="get lat and long information", action="store_true")
    args = parser.parse_args()
    
    img_path = os.path.join(os.getcwd(),'imgs_de')
    resize_path = os.path.join(os.getcwd(),'imgs_de_resized')
    augm_path = os.path.join(os.getcwd(),'imgs_de_augment')
    np_file_path = os.path.join(os.getcwd(),'imgs_npy_file')
    map_path = os.path.join(os.getcwd(),'imgs_map')

    # call imagemagick_resize() when specified in args or 'imgs_de_resized' directory not exist
    if args.resize_img or os.path.isdir(resize_path) == False:
        os.makedirs('imgs_de_resized', exist_ok=True)
        # resize image into 224*224 using imagemagick
        imagemagick_resize(img_path, resize_path)

    # call augmentor() when specified in args or 'imgs_de_augment' directory not exist
    if args.augment_img or os.path.isdir(augm_path) == False:
        os.makedirs('imgs_de_augment', exist_ok=True)
        # augment images in terms of  flip, rotation, zoom, brighteness change, saturation change, contrast change or image distortion
        augmentor(resize_path, augm_path)

    # call save_as_numpy_file() when specified in args or 'imgs_npy_file' directory not exist
    if args.save_np_file or os.path.isdir(np_file_path) == False:
        os.makedirs('imgs_npy_file', exist_ok=True)
        # read images and normalize it, save images in the same type into a .npy file with dimension (n, 224, 224, 3);
        # n is the number of images in that type folder
        save_as_numpy_file(augm_path, np_file_path)
    
    # call get_same_type_coordinates() when specified in args or 'imgs_map' directory not exist
    if args.plot_geo_info or os.path.isdir(map_path) == False:
        os.makedirs('imgs_map', exist_ok=True)
        # Etract lat and long, save into csv
        get_same_type_coordinates(img_path, map_path, save_csv = True)
    
if __name__ == '__main__':
    main()
    print("\nDone! :)") 