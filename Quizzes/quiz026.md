# Quiz 026

## Paper Solution
Paper part not uploaded to quiz slides yet.
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
