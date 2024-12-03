# Quiz 029

## Paper Solution
No paper part
## Code
```.py
import requests
from matplotlib import pyplot as plt

server_ip = "192.168.4.137"

r = requests.get(f"http://{server_ip}/readings")
a = r.json()['readings'][0]

sensor_11 = []
sensor_12 = []

for data in a:
    if data['sensor_id'] == 11:
        sensor_11.append(data['value'])
    if data['sensor_id'] == 12:
        sensor_12.append(data['value'])

plt.subplot(3, 1, 1)
plt.plot(sensor_11)

plt.subplot(3, 1, 2)
plt.plot(sensor_12)

sensor_12_temperature = []
for p in sensor_12:
    sensor_12_temperature.append((p/101) * 15) #formula from the board
plt.subplot(3, 1, 3)
plt.plot(sensor_12_temperature)

plt.show()
```
## Proof of Work
![image](https://github.com/user-attachments/assets/f410e235-c1ff-4530-b9a4-728de5c4ee96)
