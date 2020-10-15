# Simple pie chart

import matplotlib.pyplot as plt
import numpy as np
labels=('python','c++','java','Pearl')
size=[215,130,245,210]
colors=['gold','yellowgreen','red','lightskyblue']
explode = (0.1,0,0,0)

plt.pie(size,explode=explode,labels=labels,colors=colors,shadow=True,startangle = 140)
plt.axis('equal')
plt.show()
