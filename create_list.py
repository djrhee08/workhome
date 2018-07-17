import numpy as np

dir_image = 'image'
dir_mask = 'mandible'
dir_train = 'training'
dir_valid = 'validation'

tt = np.ones([512,512], dtype=np.int16)

for i in range(5):
    num = str(i+1).zfill(4)
    for j in range(180):
        num2 = str(j+1)
        np.save(dir_image + '/' + dir_train + '/' + 'image_Brain1IMRT' + num + '_' + num2 + '.npy', tt)

        if j > 30 and j < 80:
            np.save(dir_mask + '/' + dir_train + '/' + 'Mandible_mask_Brain1IMRT' + num + '_' + num2 + '.npy', tt)