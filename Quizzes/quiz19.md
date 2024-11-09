# Quiz 019

## Paper Solution

## Code
```.py
import random
random.seed(1234)

def produce(n = 5 , m = 3, s = 2):

    output = f'| {"x".center(4)} | {"y(x)".center(6)} |\n'
    for i in range(n):
        r = random.randint(0, 100)
        output += f'| {str(r).center(4)} | {f"{r ** (1 / 2 * (m / s) ** 2):.2f}".center(6)} |\n'

    return output

print(produce(n = 5 , m = 3, s = 2))
```
## Proof of Work
![image](https://github.com/user-attachments/assets/ff6e895f-0715-4b51-aa40-88dbaed02f32)

