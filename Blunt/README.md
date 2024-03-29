# Blunt
* **Event:** Cyber Apocalypse 2024
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Easy

## Description
Valuing your life, you evade the other parties as much as you can, forsaking the piles of weaponry and the vantage points in favour of the depths of the jungle. As you jump through the trees and evade the traps lining the forest floor, a glint of metal catches your eye. Cautious, you creep around, careful not to trigger any sensors. Lying there is a knife - damaged and blunt, but a knife nonetheless. You’re not helpless any more.


## Steps
#### Step 1
From the provided source code, it appears to be an attempt to implement the Diffie-Hellman key exchange. The objective is to retrieve the private key a in order to compute C.

#### Step 2
It's noted that while discrete logarithm is typically hard, the value employed here is relatively small. With the assistance of SageMath, determining the discrete logarithm becomes feasible. Consequently, we can recover C (utilized as the AES key) and decrypt the flag. Below is the script utilized for decryption.


## Code
```python
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
from hashlib import sha256

# Given values
p = 0xdd6cc28d
g = 0x83e21c05
A = 0xcfabb6dd
B = 0xc4a21ba9
ciphertext = b'\x94\x99\x01\xd1\xad\x95\xe0\x13\xb3\xacZj{\x97|z\x1a(&\xe8\x01\xe4Y\x08\xc4\xbeN\xcd\xb2*\xe6{'


a = discrete_log(A, Mod(g,p))
C = pow(B, a, p)

hash = sha256()
hash.update(long_to_bytes(int(C)))
key = hash.digest()[:16]
iv = b'\xc1V2\xe7\xed\xc7@8\xf9\\\xef\x80\xd7\x80L*'
cipher = AES.new(key, AES.MODE_CBC, iv)
msg = cipher.decrypt(ciphertext)
print(f'{msg = }')

```


#### FLAG
```
HTB{y0u_n3ed_a_b1gGeR_w3ap0n!!}
```