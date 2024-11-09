# Quiz 017

## Paper Solution
![image](https://github.com/user-attachments/assets/7b0741ed-0d4d-4e6b-b15e-206440276078)

## Code
```.py
a, b, c = 0, 0, 0
out = '| A | B | C |\n'
for i in range(1, 8+1):
    out += f'| {a} | {b} | {c} |\n'
    c = int(not c)
    if i % 2 == 0:
        b = int(not b)
    if i % 4 == 0:
        a = int(not a)
print(out)
```
## Proof of Work
![image](https://github.com/user-attachments/assets/fc788506-e835-443f-b93e-cd08bedfe057)


