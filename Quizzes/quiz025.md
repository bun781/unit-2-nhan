# Quiz 025

## Paper Solution
4 ** 3 = 64 different colors
## Code
```.py
def count_letters(my_dict:dict, msg):
    for key in my_dict.keys():
        for letter in msg:
            if key == letter:
                my_dict[key] += 1
    return my_dict
print(count_letters({"w":0,"l":0,"c":0}, "hello world"))
print(count_letters({"a":0,"e":0,"i":0,"o":0,"u":0},"Why did I choose CS"))
```
## Proof of Work
![image](https://github.com/user-attachments/assets/fcf9a061-864b-43ed-9623-b5dc0ecded7b)
