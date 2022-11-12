from tqdm import tqdm
from glob import glob
import os.path
from PIL import Image
import numpy as np
from mmcv.image import tensor2imgs
import torch

train_dir = '/home/oiocha/maicon/data/my_dataset/train'
val_dir = '/home/oiocha/maicon/data/my_dataset/val'
folder_list = ['label_1', 'label_2', 'label_3']

# print(len(input_list)) # train set : 12000, test set : 2338

def f(x):
    if x: return 255
    else: return 0
for folder in folder_list:

    input_list = glob(os.path.join(val_dir, folder, '*.png'))
    for input_path in tqdm(input_list):
        image = np.asarray(Image.open(input_path))
        #image = np.vectorize(f)(image).astype('uint8')
        image = np.expand_dims(image, axis=0).astype(np.uint8)
        Image.fromarray(image).save(input_path)

