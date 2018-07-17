import numpy as np
import os, glob
import random

maskname = "Mandible"
masklist = 'training_list.dat'
imagelist = 'image_training_list.dat'

percent_no_image = 0.8

total_list = []
pID_list = []
min_max_list = []

with open(masklist, 'r') as mask_list:
    lines = mask_list.readlines()
    for i in lines:
        temp = i.split('.')[0].split('_')
        pID = temp[-2]
        slice_num = int(temp[-1])

        # find the minimum and maximum slice number having mask slice in each patient image
        if pID not in pID_list:
            pID_list.append(pID)
            min_max_list.append([slice_num, slice_num])
        else:
            index = pID_list.index(pID)
            if min_max_list[index][0] > slice_num:
                min_max_list[index][0] = slice_num
            if min_max_list[index][1] < slice_num:
                min_max_list[index][1] = slice_num

        image_name = 'image_' + pID + '_' + str(slice_num) + '.npy'
        label = 1

        ind_list = [image_name, label]
        total_list.append(ind_list)



image_total_list = []
image_pID_list = []
image_min_max_list = []

with open(imagelist, 'r') as image_list:
    lines = image_list.readlines()
    for i in lines:
        temp = i.split('.')[0].split('_')
        pID = temp[-2]
        slice_num = int(temp[-1])

        # find the minimum and maximum slice number having mask slice in each patient image
        if pID not in image_pID_list:
            image_pID_list.append(pID)
            image_min_max_list.append([slice_num, slice_num])
        else:
            index = image_pID_list.index(pID)
            if image_min_max_list[index][0] > slice_num:
                image_min_max_list[index][0] = slice_num
            if image_min_max_list[index][1] < slice_num:
                image_min_max_list[index][1] = slice_num

        image_total_list.append(i.strip('\n'))


for i, pID in enumerate(pID_list):
    if random.random() > percent_no_image:
        print(pID)
        index = image_pID_list.index(pID)

        for slice_num in range(image_min_max_list[index][0], (image_min_max_list[index][1] + 1)):
            if slice_num < min_max_list[i][0] or slice_num > min_max_list[i][1]:
                label = 0
                ind_list = ["image_" + pID + "_" + str(slice_num) + ".npy", label]
                total_list.append(ind_list)



np.save(maskname + "_classification.npy", total_list)
