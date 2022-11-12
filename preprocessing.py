from tqdm import tqdm
from glob import glob
import os.path
from PIL import Image

before_dir='/home/oiocha/maicon/test/x'
after_dir='/home/oiocha/maicon/data/my_dataset/test'

input_list=glob(os.path.join(before_dir, '*.png'))
#print(len(input_list)) # train set : 12000, test set : 2338

for input_path in tqdm(input_list):
    image=Image.open(input_path)
    image_name=input_path.split('/')
    #print(image.size) # (1508, 754)
    w=image.size[0]
    h=image.size[1]
    croppedImage1=image.crop((0,0,w/2,h))
    croppedImage2=image.crop((w/2,0,w,h))
    
    # Saving as ".png"
    croppedImage1.save(os.path.join(after_dir,'img1_dir',image_name[-1]))
    croppedImage2.save(os.path.join(after_dir,'img2_dir',image_name[-1]))
