# Quiz 020

## Paper Solution
![image](https://github.com/user-attachments/assets/df24a7bf-16ca-4d0f-93f7-d3d57ee999a4)

## Code
```.py
import random
random.seed(1234)

from matplotlib import pyplot as plt
def produce(n = 5 , m = 3, s = 2):
    x, y = [], []
    for i in range(n):
        r = random.randint(0, 100)
        x.append(r)
        y.append(r ** (1 / 2 * (m / s) ** 2))

    return x, y

x, y  = produce(n = 5 , m = 3, s = 2)

plt.plot(x, y)
plt.show()
```

## Proof of Work
![image](https://github.com/user-attachments/assets/9e4cd20f-5cae-4fde-9244-7334a0f8cdd5)
