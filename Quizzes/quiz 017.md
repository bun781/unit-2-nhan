# Quiz 017

## Paper Solution

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
![Uploading image.png…]()

