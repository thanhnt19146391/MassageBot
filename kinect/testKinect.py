import matplotlib.pyplot as plt
import numpy as np

FOLDER = './depth_frames/'
    a = np.load(f)

plt.imshow(a)
plt.colorbar()
plt.show()