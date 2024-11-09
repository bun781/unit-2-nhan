# Quiz 023

## Paper Solution
![image](https://github.com/user-attachments/assets/d7951f44-3109-4385-8054-ef9771164d89)

## Code
```.py
from matplotlib import pyplot as plt
import numpy as np

#data set
y = [57.0, 56.0, 57.0, 56.0, 55.0, 55.0, 54.0, 54.0, 54.0, 53.0, 53.0, 54.0, 53.0, 53.0, 52.0, 52.0, 51.0, 51.0, 51.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 48.0, 49.0, 49.0, 48.0, 48.0, 48.0, 49.0]
x = []
for i in range(len(y)):
    x.append(i)

m, b = np.polyfit(x, y, 1)
print(f'The linear model for the data is H_model = {m:.2f}x + ({b:.2f})')

#graph plot
def model(x, m, b):
    return m*x + b #returns the linear equation

x_model = [min(x), max(x)] #min and max of the list named "x"
y_model = [model(min(x), m, b), model(max(x), m, b)] #m and b found from the numpy polyfit

#graph legend
plt.title('Humidity Data')
plt.xlabel('Time')
plt.ylabel('Relative Humidity')

#plot model
plt.plot(x_model, y_model, label = 'ball', color = 'red')

#scatter
plt.scatter(x,y)

#show plot
plt.show()

```
## Proof of Work
![image](https://github.com/user-attachments/assets/3c0a70e8-0014-4c52-8bd3-9bd9b56445d2)

