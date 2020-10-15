# 1-x2/2
import matplotlib.pyplot as plt
import numpy as np
xvals= np.arange(-2,1,0.01)
yvals= 1 - ((xvals)**2)/2
plt.plot(xvals,yvals)
plt.show()
