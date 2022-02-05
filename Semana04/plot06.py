import matplotlib.pyplot as plt 
import numpy as np

x1 = np.arange(-1000, 1000, 1)
x2 = x1**2
plt.plot(x1, x2)
plt.plot(x1, (x1**3)+4)
plt.show()
