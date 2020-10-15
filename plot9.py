# Simple bar chart

import matplotlib.pyplot as plt
import numpy as np
y= np.arange(1,3)

plt.plot(y,'--')
plt.plot(y+1,'-.')
plt.plot(y+2,':')
plt.show()
