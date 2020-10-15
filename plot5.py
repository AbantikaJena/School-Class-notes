# program for plotting sine waves
import matplotlib.pyplot as plt
import numpy as np
xvals= np.arange(-2,1,0.01)
yvals= np.sin(xvals)
plt.plot(xvals,yvals)
plt.show()
