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
