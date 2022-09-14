from operator import ne
import os

# Declaration
FOLDER = './yolov3/'
IMG_FOLDER = FOLDER + 'images/'
TEMP_FOLDER = FOLDER + 'temp/'
NAME = 'back'
EXT = '.jpg'

# Rename images in sequential order and count number of image
maxN = 0
for _, fullName in enumerate(os.listdir(IMG_FOLDER)):
    name, ext = fullName.split('.')
    if ext != 'txt':
        oldName = IMG_FOLDER + fullName
        newName = TEMP_FOLDER + NAME + str(maxN) + EXT
        os.rename(oldName, newName)
        maxN += 1  

# Move images to their folder
for _, fullName in enumerate(os.listdir(TEMP_FOLDER)):
    _, ext = fullName.split('.')
    oldName = TEMP_FOLDER + fullName
    newName = IMG_FOLDER + fullName
    os.rename(oldName, newName)

print('Amount of images: ', maxN)




