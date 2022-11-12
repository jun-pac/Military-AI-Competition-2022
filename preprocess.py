from tqdm import tqdm
from glob import glob
import os.path
from PIL import Image
import numpy as np

before_dir = '/home/oiocha/maicon/train/y'
after_dir = '/home/oiocha/maicon/data/my_dataset/train'

input_list = glob(os.path.join(before_dir, '*.png'))
# print(len(input_list)) # train set : 12000, test set : 2338

for input_path in tqdm(input_list):
    image = Image.open(input_path)
    image_name = input_path.split('/')
    # print(image.size) # (1508, 754)
    w = image.size[0]
    h = image.size[1]
    if w/2!=754 or h!=754:
        print((w/2, h))

    croppedImage1 = np.asarray(image.crop((0, 0, w / 2, h)))
    croppedImage2 = np.asarray(image.crop((w / 2, 0, w, h)))

    label_1 = croppedImage2==1
    label_2 = croppedImage1==2
    label_3 = croppedImage2==3
    if label_3.shape[0]!=754 or label_3.shape[1]!=754:
        print(label_3.shape)

    if int(w/2)!=label_3.shape[0] or h!=label_3.shape[1]:
        print(image_name[-1])
    # print(np.sum(label_1), np.sum(label_2), np.sum(label_3))


    # Saving as ".png"
    Image.fromarray(croppedImage1).save(os.path.join(after_dir, 'Image1', image_name[-1]))
    Image.fromarray(croppedImage2).save(os.path.join(after_dir, 'Image2', image_name[-1]))
    Image.fromarray(label_1).save(os.path.join(after_dir, 'label_1', image_name[-1]))
    Image.fromarray(label_2).save(os.path.join(after_dir, 'label_2', image_name[-1]))
    Image.fromarray(label_3).save(os.path.join(after_dir, 'label_3', image_name[-1]))