# Quiz 026

## Paper Solution
![image](https://github.com/user-attachments/assets/7e155663-b2c1-4894-ab93-a40cd2d6ba64)

## Code
```.py
def flip(in_dict):
    out_dict = {}
    for key, value in in_dict.items():
        out_dict[value] = [out_dict[value]] + [key] if value in out_dict else key
    return out_dict

print(flip({'q1':True,'q2':False,'q3':True}))
print(flip({"bob":26,"alice":30,"carl":40}))
```
## Proof of Work
