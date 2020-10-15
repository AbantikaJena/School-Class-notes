# Simple horizontal bar chart

import matplotlib.pyplot as plt
import numpy as np
object=('python','c++','java','Pearl','Scala','Lisp')
y_axis = np.arange(len(object))
performance =[10,8,6,4,2,1]
plt.barh(y_axis,performance,align='center',color='r')
plt.yticks(y_axis,object)
plt.xlabel('Usage')
plt.title('Programing Language usage')
plt.show()
