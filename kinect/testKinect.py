import matplotlib.pyplot as plt
import numpy as np

with open('10.npy', 'rb') as f:
    a = np.load(f)

plt.imshow(a)
plt.colorbar()
plt.show()