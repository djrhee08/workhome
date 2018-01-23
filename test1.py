import dicom
import numpy as np
import skimage.transform as sktf
import matplotlib.pyplot as plt
import math

def bitresample(dcmimage, bit=8):
    dcmimage = np.matrix.round(dcmimage / bit)
    dcmimage = dcmimage * bit

    return dcmimage

def resize(dcmimage, resize_shape=(227,227)):
    if dcmimage.shape != (512,512):
        print("The size of DICOM is not 512 X 512. Please check again!")
        return

    return sktf.resize(dcmimage, resize_shape, mode="constant")

def rotate(dcmimage, angle):
    return sktf.rotate(dcmimage,angle=angle)

file = dicom.read_file("dicom1.dcm")
dcmimage = file.pixel_array
if hasattr(file, 'RescaleSlope'):
    slope = file.RescaleSlope
else:
    slope = 1
if hasattr(file, 'RescaleIntercept'):
    intercept = file.RescaleIntercept
else:
    intercept = 0

dcmimage = dcmimage * slope + intercept
dcmresize = resize(dcmimage)
print(dcmimage.max(), dcmimage.min())
print(dcmresize.max(), dcmresize.min())

dcmimage2 = rotate(dcmimage,80)
"""
print(dcmimage.shape)
print(dcmimage[254:256,254:256])
print(dcmimage2[254:256,254:256])

mask = np.zeros([512,512])
mask[250:260, 250:260] = True
mask2 = rotate(mask, 80)
print(mask[250:260,250:260])
print(mask2[250:260,250:260])



plt.subplot(1,4,1)
plt.imshow(dcmimage,cmap='gray')
plt.subplot(1,4,2)
plt.imshow(dcmimage2,cmap='gray')
plt.subplot(1,4,3)
plt.imshow(mask,cmap='gray')
plt.subplot(1,4,4)
plt.imshow(mask2,cmap='gray')
plt.show()

"""