# Quiz 018

## Paper Solution
![image](https://github.com/user-attachments/assets/489ca931-4c44-4e75-92b2-eb6e2ca53e92)

## Code
```.py
a, b, c = 0, 0, 0
out = '| A | B | C | AB + (not B) + not(CB) |\n'
for i in range(1, 8+1):
    out += f'| {a} | {b} | {c} | {str(int((a and b) or (not b) or (not(c and b)))).center(22)} |\n'
    c = int(not c)
    if i % 2 == 0:
        b = int(not b)
    if i % 4 == 0:
        a = int(not a)
print(out)
```
## Proof of Work
![image](https://github.com/user-attachments/assets/8cc7fb56-137b-4ff1-bb35-a1cb8b4f5f22)
