from tqdm import tqdm
from glob import glob
import os.path
from PIL import Image
'''
label_path='/home/oiocha/maicon/data/my_dataset/train/label_dir/2015_DMG_1LB_000006.png'
image=Image.open(label_path)
image=image.convert('RGB')

# Make transform matrix, to multiply R by 1.5, leaving G and B unchanged
Matrix = ( 50, 0, 0, 0, 
           0, 50, 0, 0, 
           0, 0, 50, 0) 

# Apply transform and save 
image = image.convert("RGB", Matrix) 

#image=image*10
image_name=label_path.split('/')
image.save(os.path.join("/home/oiocha/maicon/data/my_dataset/lighted_up",image_name[-1]))
'''


#label_dir='/home/oiocha/maicon/data/my_dataset/train/label_dir'
label_dir='/home/oiocha/maicon/submit'
label_list=glob(os.path.join(label_dir, '*.png'))
for label_path in tqdm(label_list):
    image=Image.open(label_path)
    image=image.convert('RGB')

    # Make transform matrix, to multiply R by 1.5, leaving G and B unchanged
    Matrix = ( 80, 0, 0, 0, 
                0, 80, 0, 0, 
                0, 0, 80, 0) 

    # Apply transform and save 
    image = image.convert("RGB", Matrix) 

    #image=image*10
    image_name=label_path.split('/')
    image.save(os.path.join("/home/oiocha/maicon/data/my_dataset/lighted_up",image_name[-1]))
