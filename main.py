from utils.resize import imagemagick_resize
import os
import argparse

def main():
    """
    Image processing pipeline
    """
    parser = argparse.ArgumentParser()  
    parser.add_argument("-R", "--resize_img", help="resize the image in imgs_de/", action="store_true")
    args = parser.parse_args()
    
    img_path = os.path.join(os.getcwd(),'imgs_de')
    resize_path = os.path.join(os.getcwd(),'imgs_de_resized')

    # call imagemagick_resize() when specified in args or no image is resized
    if args.resize_img or os.path.isdir(resize_path) == False:
        os.makedirs('imgs_de_resized', exist_ok=True)
        imagemagick_resize(img_path, resize_path)


if __name__ == '__main__':
    main()
    print("\nDone! :)") 
    print(repr(imagemagick_resize.__doc__))