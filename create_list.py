import numpy as np

dir_image = 'image'
dir_mask = 'mask'
dir_train = 'training'
dir_valid = 'validation'

tt = np.ones([512,512])

for i in range(5):
    num = str(i+1).zfill(4)
    for j in range(200):
        num2 = str(j+1)
        np.save(dir_image + '/' + dir_valid + '/' + 'image_Brain2IMRT' + num + '_' + num2 + '.npy', tt)

        if j > 30 or j < 80:
            np.save(dir_mask + '/' + dir_valid + '/' + 'Mandible_mask_Brain2IMRT' + num + '_' + num2 + '.npy', tt)