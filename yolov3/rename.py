import os

# Declaration
FOLDER = './yolov3/'
IMG_FOLDER = FOLDER + 'images/'
TEMP_FOLDER = FOLDER + 'temp/'
NAME = 'back'
JPG_EXT = '.jpg'
IMG_EXT = ['jpg', 'png']

# Rename image files and txt files in sequential order 
maxN = 0
for i, fullName in enumerate(os.listdir(IMG_FOLDER)):
    name, ext = fullName.rsplit('.', 1)
    if ext in IMG_EXT:
        old_txtName = IMG_FOLDER + name + '.txt'
        new_txtName = TEMP_FOLDER + NAME + str(maxN) + '.txt'
        oldName = IMG_FOLDER + fullName
        newName = TEMP_FOLDER + NAME + str(maxN) + JPG_EXT
        maxN += 1
        os.rename(oldName, newName)
        if os.path.exists(old_txtName):
            os.rename(old_txtName, new_txtName)   
    
# Delete file .txt without classes.txt
for i, fullName in enumerate(os.listdir(IMG_FOLDER)):
    name, ext = fullName.split('.')
    if name != 'classes' and ext == 'txt':
        fileName = IMG_FOLDER + fullName
        os.remove(fileName)

# Move images to their folder
for _, fullName in enumerate(os.listdir(TEMP_FOLDER)):
    _, ext = fullName.split('.')
    oldName = TEMP_FOLDER + fullName
    newName = IMG_FOLDER + fullName
    os.rename(oldName, newName)

print('Amount of images: ', maxN)




