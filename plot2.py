# program to draw two lines along with proper titles and legends
import matplotlib.pyplot as plt
x=[1,2,3]
y=[5,6,7]
plt.plot(x,y,label = "First Line")
x2= [1,2,3]
y2= [10,11,14]
plt.plot(x2,y2,label = "Second Line")
plt.xlabel("Plot number")
plt.ylabel("important variables")
plt.title("New Graph")
plt.legend()
plt.show()
