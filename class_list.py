import numpy as np
import os, glob

dir_image = 'image'
dir_mask = 'mask'
dir_train = 'training'
dir_valid = 'validation'

training = dir_mask + '/' + dir_train + '/*.npy'
validation = dir_mask + '/' + dir_valid + '/*.npy'

training_list = 'training_list.dat'
validation_list = 'validation_list.dat'
image_list = 'image_list.dat'

with open(training_list, 'r') as train_list, open(validation_list, 'r') as valid_list:
    lines = train_list.readlines()
    for i in lines:
        temp = i.split('\\')[0].split('.')[0]
        maskname = '_'.join(temp.split('_')[-2:])

        lines2 = valid_list.readlines()
        for j in lines2:
            temp = j.split('\\')[0].split('.')[0]
            imgname = '_'.join(temp.split('_')[-2:])

            print(maskname, imgname)
            if maskname == imgname:
                print(maskname)


