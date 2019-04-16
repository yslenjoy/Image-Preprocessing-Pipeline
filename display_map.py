"""Map the locations of the images in given dataset
"""

from PIL import Image
from PIL.ExifTags import GPSTAGS
from PIL.ExifTags import TAGS
import matplotlib.pyplot as plt
import numpy as np
from utils.make_sub_dir import folder_is_hidden
import os
from os.path import join
import pandas as pd


def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()

def get_geotagging(exif):
    if not exif:
        # raise ValueError("No EXIF metadata found")
        # if no exif infor, exit the function
        return

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")

            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]

    return geotagging

def get_decimal_from_dms(dms, ref):
    degrees = dms[0][0] / dms[0][1]
    minutes = dms[1][0] / dms[1][1] / 60.0
    seconds = dms[2][0] / dms[2][1] / 3600.0

    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds

    return round(degrees + minutes + seconds, 5)

def get_img_coordinates(geotags):
    lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])

    lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

    return [lat,lon]

def get_same_type_coordinates(img_dir, out_dir, save_csv = True):
    """Get all the coordinates of images in img_dir directory.

    Args:
        img_dir(string): original image directory. In img_dir, different kinds of vegetations are stored in subdirectories (e.g img_dir/corn/image1.jpg)
        output(string): the directory where .npy file will be saved.
    Returns:
        types(list of string): store the names of the vegetation type
        df(dataFrame): (lat, long, IMAGE_NAME, veg_type)
    """
    types = [f for f in os.listdir(img_dir) if not folder_is_hidden(f)]

    all_type_coord = []
    for t in types:
        in_path = join(img_dir, t)
        images = [i for i in os.listdir(in_path) if not folder_is_hidden(i)]

        # single_type_coord = []
        for j in range(len(images)):
            exif = get_exif(join(in_path, images[j]))
            if exif: # if exif data can be found in image
                geotags = get_geotagging(exif)
                result = get_img_coordinates(geotags)
                # add image name
                result.append(images[j])
                # add veg type
                result.append(t)
                all_type_coord.append(result)
                # print(result)
        print('Extract coordinates from images in {}...'.format(t))
        # all_type_coord.append(single_type_coord)
    df = pd.DataFrame.from_records(all_type_coord)
    df.columns = ['latitude', 'longitude', 'img_name', 'veg_type']
    if save_csv:
        out_path = join(out_dir, 'image_geo_info.csv')
        df.to_csv(out_path, index=False)
        print('Geolocation information saved in {}'.format(out_path))

    
    # some weird things: 'Class QCocoaPageLayoutDelegate is implemented in both...' will happen in my mac, but image still saves
    groups = df.groupby('veg_type')
    # Plot
    fig, ax = plt.subplots()
    for name, group in groups:
        ax.plot(group.latitude, group.longitude, marker='o', linestyle='', ms=12, label=name)
    ax.legend()
    fig.savefig(join(out_dir, 'location_map.jpg'))
    
    return types, df






