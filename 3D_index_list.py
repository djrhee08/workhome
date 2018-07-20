import numpy as np
import os, glob
from sys import argv

if len(argv) == 1:
    dir_name1 = 'training/'
    dir_name2 = 'validation/'
    mat_files1 = dir_name1 + '*.mat'
    mat_files2 = dir_name2 + '*.mat'
    print("dir_name : ", dir_name1, ', ', dir_name2)
else:
    dir_name1 = argv[1] + '/'
    mat_files1 = dir_name1 + '*.mat'
    print("dir_name : ", dir_name1)


mask_list = 'mask_slice_index.dat'
image_list = 'image_slice_index.dat'

with open(dir_name1 + mask_list, 'w') as f, open(dir_name1 + image_list, 'w') as f2:
    for i in sorted(glob.glob(mat_files1)):
        mask_name = i.split('/')[-1]
        f.write(mask_name+'\n')

        image_name = '3D_image_' + mask_name.split('_')[-1]
        f2.write(image_name+'\n')


if len(argv) == 1:
    with open(dir_name2 + mask_list, 'w') as f, open(dir_name2 + image_list, 'w') as f2:
        for i in sorted(glob.glob(mat_files2)):
            mask_name = i.split('/')[-1]
            f.write(mask_name+'\n')

            image_name = '3D_image_' + mask_name.split('_')[-1]
            f2.write(image_name+'\n')
