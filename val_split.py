import os, shutil
from glob import glob
from sklearn.model_selection import train_test_split

train_dirs = '/home/oiocha/maicon/data/my_dataset/train'
val_dirs = '/home/oiocha/maicon/data/my_dataset/val'

Img1_paths = glob(os.path.join(train_dirs, 'Image1', '*.png'))
Img2_paths = glob(os.path.join(train_dirs, 'Image2', '*.png'))
_, val_img_paths = train_test_split(Img1_paths, test_size=0.05, random_state=42, shuffle=True)

folder_list = ['Image1', 'Image2', 'label_dir', 'label_1', 'label_2', 'label_3']

for path in val_img_paths:
    for folder in folder_list:
        shutil.move(path.replace('Image1', folder), path.replace('train', 'val').replace('Image1', folder))

# reset
'''
for folder in folder_list:
    for file in glob(os.path.join(val_dirs, folder, '*.png')):
        shutil.move(file, file.replace('val', 'train'))
'''