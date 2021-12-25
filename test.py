import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()


L_x = np.array([1,2,3])
L_y = 2*L_x+3



ax.plot(L_x, L_y, color='green', label='SMA5')
plt.legend()
plt.show()