from utils.resize import imagemagick_resize
import os

def main():
    """
    Image processing pipeline
    """

    # Resize images into 224 * 224 using imagemagick,
    # resized images are stored in imgs_de_resized/
    os.makedirs('imgs_de_resized', exist_ok=True)
    img_path = os.path.join(os.getcwd(),'imgs_de')
    resize_path = os.path.join(os.getcwd(),'imgs_de_resized')

    imagemagick_resize(img_path, resize_path)

if __name__ == '__main__':
    main()
    print("\nDone! :)") 