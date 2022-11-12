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


def distrib_func(idx):
    cnt1=0
    cnt2=0
    cnt3=0
    for i in range(idx,min(idx+chunk_size,N)):
        result_path=result_list[i]
        image=Image.open(result_path)
        w,h=image.size
        px = image.load()
        
        for i in range(w):
            for j in range(h):
                if(px[i,j]==1):
                    cnt1+=1
                elif(px[i,j]==2):
                    cnt2+=1
                elif(px[i,j]==3):
                    cnt3+=1
        
    print(f"PID : {os.getpid()}  |  [{idx}, {min(idx+chunk_size,N)})th images finished  |  Time : {time.time()-t0:.5f}s")
    return (cnt1,cnt2,cnt3)

with Pool(core_cnt) as p:
    result=p.map(distrib_func, range(0,N,chunk_size))

tot_cnt1=0
tot_cnt2=0
tot_cnt3=0
for c1,c2,c3 in result:
    tot_cnt1+=c1
    tot_cnt2+=c2
    tot_cnt3+=c3
tot_sum=tot_cnt1+tot_cnt2+tot_cnt3
f_log=open("/home/oiocha/maicon/sejun/distibution.txt","w+")
print(f"First {N} datas | tot_cnt1 : {tot_cnt1}({tot_cnt1/tot_sum*100:.2f}%), tot_cnt2 : {tot_cnt2}({tot_cnt2/tot_sum*100:.2f}%), tot_cnt3 : {tot_cnt3}({tot_cnt3/tot_sum*100:.2f}%)")
f_log.write(f"First {N} datas | tot_cnt1 : {tot_cnt1}({tot_cnt1/tot_sum*100:.2f}%), tot_cnt2 : {tot_cnt2}({tot_cnt2/tot_sum*100:.2f}%), tot_cnt3 : {tot_cnt3}({tot_cnt3/tot_sum*100:.2f}%)\n")
f_log.flush()