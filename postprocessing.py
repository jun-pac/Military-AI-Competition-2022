from tqdm import tqdm
from glob import glob
import os.path
import os
from PIL import Image
from multiprocessing import Pool, Process, Array
import time

chunk_size=60
core_cnt=64
t0=time.time()

result_dir='/home/oiocha/maicon/data/my_dataset/train/label_dir' # For test
result_list=glob(os.path.join(result_dir, '*.png'))
N=len(result_list)
submit_dir='/home/oiocha/maicon/submit'

# Please check directory!
assert result_dir is not '/home/oiocha/maicon/data/my_dataset/train/label_dir'
assert submit_dir is not '/home/oiocha/maicon/submit'

def mask_func(idx):
    for i in range(idx,min(idx+chunk_size,N)):
        result_path=result_list[i]
        image=Image.open(result_path)
        w,h=image.size
        px = image.load()
        # left-side
        for i in range(w//2):
            for j in range(h):
                if(px[i,j]==1 or px[i,j]==3):
                    px[i,j]=0

        # right-side
        for i in range(w//2,w):
            for j in range(h):
                if(px[i,j]==2):
                    px[i,j]=0


        image_name=result_path.split('/')
        image.save(os.path.join(submit_dir,image_name[-1]))

    print(f"PID : {os.getpid()}  |  [{idx}, {min(idx+chunk_size,len(result_list))})th images finished  |  Time : {time.time()-t0:.5f}s")

with Pool(core_cnt) as p:
    p.map(mask_func, range(0,N,chunk_size))