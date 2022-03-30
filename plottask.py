# the libraries numpy and matplotlib are imported
import numpy as np
import matplotlib.pyplot as plt
# x-axis values (starting value, ending value and step size)
x = np.arange(0.0, 4.0, 0.5)
# y-axis values
# the functions f(x), g(x), and h(x) are calculated as outlined in the task
f = x      
g = x**2   
h = x**3 
# plotting f, g and h separately
# red line
plt.plot(f,f, '-r', marker='o', label = 'f(x)=x') 
# blue line 
plt.plot(f,g, '--b', marker= 'x',  label = 'g(x)= x2')
# green line
plt.plot(f,h, '-.g', marker= 's', label = 'h(x)=x3')

plt.ylabel('Y-AXIS')
plt.xlabel('X-AXIS')
plt.title ('Functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] ')
plt.legend()
# saving
plt.savefig("plottask.png")
# displaying the plot
plt.show()