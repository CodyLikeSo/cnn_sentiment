from PIL import Image
import os
import numpy as np

def resize(folder_path, resized_folder_path):
    if not os.path.exists(resized_folder_path):
        os.makedirs(resized_folder_path)

    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            img_resized = img.resize((224, 224), Image.LANCZOS)
            resized_img_path = os.path.join(resized_folder_path, filename)
            img_resized.save(resized_img_path)



def count_files(dir_path):
    count = 0
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    print('File count:', count)

    # print(f'{round(count*0.7)} for train')
    # print(f'{round(count*0.2)} for test')
    # print(f'{round(count*0.1)} for valid')
    return count