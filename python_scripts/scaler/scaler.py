from getcolor import get_colors
import os
from shutil import copyfile

def sort_by_rgb(folder):

    image_list_colors = {}

    directory = f'/home/brujxs/Documents/scaler/{folder}'

    for count, image in enumerate(os.listdir(directory)):

        if not image.endswith('.jpg'):
            continue
        else:
            current_image_colors = get_colors(f"{folder}/"+image)

            values_to_sum = current_image_colors[0]

            average_color_value= sum(values_to_sum)

            image_list_colors |= {image:average_color_value}

        sorted_list = dict(sorted(image_list_colors.items(), key=lambda item: item[1]))

        sorted_list_keys = list(sorted_list.keys())

    return sorted_list_keys






def copy_sorted_to_our_folder(source_folder, new_folder):

    ordered_images = sort_by_rgb(f'{source_folder}')

    if not os.path.isdir(f"/{source_folder}/{new_folder}"):
        os.mkdir(f"/{source_folder}/{new_folder}")

    for count, image_to_order in enumerate(ordered_images):
        if image_to_order.endswith('jpg'):
            dst = f"{str(count)}.jpg"
            src =  f"{source_folder}/{image_to_order}"
            dst = f"{source_folder}/{new_folder}/{count}_copy.jpg" 
            copyfile(src, dst)
            print(src)
            print(dst)
        else:
            continue

copy_sorted_dict('images','sorted_images')