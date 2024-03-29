# Makeshift
* **Event:** Cyber Apocalypse 2024
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Very Easy

## Description
Weak and starved, you struggle to plod on. Food is a commodity at this stage, but you can’t lose your alertness - to do so would spell death. You realise that to survive you will need a weapon, both to kill and to hunt, but the field is bare of stones. As you drop your body to the floor, something sharp sticks out of the undergrowth and into your thigh. As you grab a hold and pull it out, you realise it’s a long stick; not the finest of weapons, but once sharpened could be the difference between dying of hunger and dying with honour in combat.


## Steps
#### Step 1
The encryption is quite straightforward, We can simply re-arranged per 3 characters, then reverse it.

## Code
```python
encoded_flag = "!?}De!e3d_5n_nipaOw_3eTR3bt4{_THB"
decoded_flag = ''

# Reverse the string
reversed_flag = encoded_flag[::-1]

# Rearrange characters in groups of three
for i in range(0, len(reversed_flag), 3):
    decoded_flag += reversed_flag[i+1]
    decoded_flag += reversed_flag[i+2]
    decoded_flag += reversed_flag[i]

print(decoded_flag)

```


#### FLAG
```
HTB{4_b3tTeR_w3apOn_i5_n3edeD!?!}
```