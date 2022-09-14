import matplotlib.pyplot as plt
import numpy as np

FOLDER = './depth_frames/'

fileName = FOLDER + '10.npy'
with open(fileName, 'rb') as f:
    a = np.load(f)

plt.imshow(a)
plt.colorbar()
plt.show()