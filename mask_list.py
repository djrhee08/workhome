import numpy as np
import os, glob

mask_list = 'mask_slice_index.dat'
image_list = 'image_slice_index.dat'

npy_files = '*.npy'

with open(mask_list, 'w') as f:
    for i in glob.glob(npy_files):
        temp = i.replace('\\','/')
        temp = temp.split('/')[-1]
        f.write(temp+'\n')

with open(valid_list, 'w') as f:
    for i in glob.glob(validation):
        temp = i.replace('\\','/')
        temp = temp.split('/')[-1]
        f.write(temp+'\n')
