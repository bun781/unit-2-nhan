# Quiz 022

## Paper Solution
![image](https://github.com/user-attachments/assets/225db91f-83a6-4f85-8973-d6d2bd784470)

## Code
```.py
from matplotlib import pyplot as plt
plt.style.use('ggplot')

start = -10
step = 0.01

x = []
y = []

for i in range(int(20/step)):
    x.append(start + step*i)
    y.append(abs(x[-1]))

plt.xlabel('x')
plt.ylabel('$f\left(x\\right)\ =\ \left|x\\right|$')
plt.plot(x,y)
plt.show()
```
## Proof of Work
![image](https://github.com/user-attachments/assets/d3ea8dec-19d8-4781-aa2e-09b228aa722e)

