# Quiz 027

## Paper Solution
![image](https://github.com/user-attachments/assets/2b176d70-503a-4f50-8ef3-4931b8aed318)

## Code
```.py
def sort_dict(in_dict):
    flip_dict = {}
    for key, value in in_dict.items():
        flip_dict[value] = [flip_dict[value]] + [key] if value in flip_dict else key
    out_dict_2 = {}
    a = sorted(map(str, flip_dict.keys()))
    for key in a:
        if key in '0123456789':
            out_dict_2[flip_dict[int(key)]] = key
        else:
            out_dict_2[flip_dict[key]] = key

    return out_dict_2

print(sort_dict({'apple': 'red', 'banana': 2, 'orange': 'orange', 'grape': 1, 'kiwi': 'brown', 'pear': 8}))
```
## Proof of Work
![image](https://github.com/user-attachments/assets/0f433b64-8df9-4097-aff3-09453761ba21)
