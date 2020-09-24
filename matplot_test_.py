import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline

x = np.arange(0,10)
y = np.arange(11,21) 

#plt.scatter(x,y,c='g')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Graph in 2D")
y= x*x
plt.plot(x,y,'ro')
plt.show()