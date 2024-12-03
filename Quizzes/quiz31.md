# Quiz 031

## Paper Solution


## Code
```.py
from matplotlib import pyplot as plt

scale = 100
x = [i/scale for i in range(-2*scale, 2*scale+1)]
y = [i**2 for i in x]
y_ = [-i for i in y]
plt.style.use('ggplot')

plt.title('Four Parabolas Aligned with Axes')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')

plt.axis('equal')
plt.plot(x, y, label = 'Parabola 1 (x-axis)')
plt.plot(x, y_, label = 'Parabola 2 (x-axis)')
plt.plot(y,x, label = 'Parabola 3 (y-axis)')
plt.plot(y_,x, label = 'Parabola 4 (y-axis)')

plt.legend()
plt.show()
```
## Proof of Work
