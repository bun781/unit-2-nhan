# Quiz 030

## Paper Solution
No paper part
## Code
```.py
from datetime import datetime
import requests
from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec

server_ip = "192.168.4.137"

a = requests.get(f'http://{server_ip}/readings')
readings = a.json()["readings"][0]
temp = []
hum = []
for r in readings:
    if r["sensor_id"] == 11:
        temp.append(r["value"])
    if r["sensor_id"] == 10:
        hum.append(r["value"])
fig = plt.figure(figsize=(10,5))
grid = GridSpec(nrows=3, ncols=4, figure=fig)

plt.subplots_adjust(hspace = 0.5)

box1 = fig.add_subplot(grid[1, 0])
plt.plot(temp, color = 'red')

sum_ = []
for i in range(len(hum)):
    sum_.append(temp[i] + hum[i])
box2 = fig.add_subplot(grid[0:3, 1:3])
plt.plot(sum_, color = 'blue')

box3 = fig.add_subplot(grid[1, 3])
plt.plot(hum, color = 'red')

plt.show()
```
## Proof of Work
![image](https://github.com/user-attachments/assets/e0d4a13b-3fa9-4c7f-a2a6-9709f0010728)
