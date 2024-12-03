# Quiz 028

## Paper Solution
No paper part
## Code
```.py
from datetime import datetime
import requests
from matplotlib import pyplot as plt
import numpy as np

def moving_average(windowSize: int, x: list) -> list:
    x_smoothed = []
    for i in range(0, len(x)-windowSize+1):
        x_section = x[i:i+windowSize+1]
        x_average = sum(x_section) / windowSize
        x_smoothed.append(x_average)
    return x_smoothed

server_ip = "192.168.4.137"

a = requests.get(f'http://{server_ip}/readings')
readings = a.json()["readings"][0]
temp = []
for r in readings:
    if r["sensor_id"] == 11:
        temp.append(r["value"])
temp = moving_average(50, temp)
c, d, e = np.polyfit([i for i in range(600, 1601)], temp[600:1601], deg = 2)

x = [i/100 for i in range(600*100, 1600*100 + 1)]
y = [c*X**2 + d*X + e for X in x]
plt.plot(x,y)
plt.plot([i for i in range(600, 1601)], temp[600:1601])
plt.show()
```
## Proof of Work
![image](https://github.com/user-attachments/assets/bd8264d0-be00-4e44-835b-55c9c6ff6c1c)
