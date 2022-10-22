# In this example, we are creating a simple linear graph that will show an animation of a Line. Similarly, using FuncAnimation, we can create many types of Animated Visual Representations. We just need to define our animation in a function and then pass it to FuncAnimation with suitable parameters.

# Syntax: FuncAnimation(figure, animation_function, frames=None, init_func=None, fargs=None, save_count=None, *, cache_frame_data=True, **kwargs)

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

x = []
y = []
  
figure, ax = plt.subplots()
  
# Setting limits for x and y axis
ax.set_xlim(0, 200)
ax.set_ylim(0, 12)
  
# Since plotting a single graph
line,  = ax.plot(0, 0) 
  
def animation_function(i):
    x.append(i * 15)
    y.append(i)
  
    line.set_xdata(x)
    line.set_ydata(y)
    return line,
  
animation = FuncAnimation(figure,
                          func = animation_function,
                          frames = np.arange(0, 10, 0.1), 
                          interval = 10)

plt.title("linear graph Data")

plt.xlabel("X label")
plt.ylabel("Y label")
plt.show()