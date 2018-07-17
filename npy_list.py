import numpy as np
import os, glob

dir_image = 'image'
dir_mask = 'mask'
dir_train = 'training'
dir_valid = 'validation'

valid_list = 'validation_list.dat'
train_list = 'training_list.dat'

training = dir_mask + '/' + dir_train + '/*.npy'
validation = dir_mask + '/' + dir_valid + '/*.npy'

with open(train_list, 'w') as f:
    for i in glob.glob(training):
        temp = i.replace('\\','/')
        temp = temp.split('/')[-1]
        f.write(temp+'\n')

with open(valid_list, 'w') as f:
    for i in glob.glob(validation):
        temp = i.replace('\\','/')
        temp = temp.split('/')[-1]
        f.write(temp+'\n')