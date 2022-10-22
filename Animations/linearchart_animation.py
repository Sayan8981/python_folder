#Using pause() function

# The pause() function in the pyplot module of the matplotlib library is used to pause for interval seconds mentioned in the argument. Consider the below example in which we will create a simple linear graph using matplotlib and show Animation in it:

# Create 2 arrays, X and Y, and store values from 1 to 100.
# Plot X and Y using plot() function.
# Add pause() function with suitable time interval
# Run the program and you’ll see the animation.

from matplotlib import pyplot as plt

x = []
y = []
  
for i in range(101):
    x.append(i)
    y.append(i)
  
    # Mention x and y limits to define their range
    plt.xlim(0, 200)
    plt.ylim(0, 200)
      
    # Ploting graph
    plt.plot(x, y, color = 'green')
    plt.pause(0.02)
  
plt.show()