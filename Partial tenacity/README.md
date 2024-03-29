# Partial tenacity
* **Event:** Cyber Apocalypse 2024
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Medium

## Description
You find yourself in a labyrinthine expanse where movement is restricted to forward paths only. Each step presents both opportunity and uncertainty, as the correct route remains shrouded in mystery. Your mission is clear: navigate the labyrinth and reach the elusive endpoint. However, there’s a twist—you have just one chance to discern the correct path. Should you falter and choose incorrectly, you’re cast back to the beginning, forced to restart your journey anew. As you embark on this daunting quest, the labyrinth unfolds before you, its twisting passages and concealed pathways presenting a formidable challenge. With each stride, you must weigh your options carefully, considering every angle and possibility. Yet, despite the daunting odds, there’s a glimmer of hope amidst the uncertainty. Hidden throughout the labyrinth are cryptic clues and hints, waiting to be uncovered by the keen-eyed. These hints offer glimpses of the correct path, providing invaluable guidance to those who dare to seek them out. But beware, for time is of the essence, and every moment spent deliberating brings you closer to the brink of failure. With determination and wit as your allies, you must press onward, braving the twists and turns of the labyrinth, in pursuit of victory and escape from the labyrinth’s confounding embrace. Are you tenacious enough for that?

## Steps
#### Step 1
We were given only the odd digits of p and the even digits of q. Our task is to devise a method to reconstruct p and q using this limited information.

#### Step 2

$$ n_i = \text{carry}_{i-1} + \sum_{j=0}^{i} p_{i-j} \times q_i $$

#### Step 3
With the above equation we can implement our Depth-First Search (DFS) strategy as follows:

1. **At the current digit, generate all possible combinations of the missing digits.**
2. **For each of these possible combinations:**
   - Insert it into the equation derived above and check:
     - If the result modulo 10 matches the known `n_i` digit, store it as a possible combination.
     - If the result modulo 10 does not match the known `n_i` digit, skip it.
3. **If the list of possible combinations has more than 0 items, proceed to the next digit.**
4. **If there are no possible combinations, backtrack to the previous digit and try a different combination.**

Once `p` and `q` are recovered using this strategy, decrypting the flag becomes straightforward.

## Code
```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Replace these with your actual values
ct = bytes.fromhex('7f33a035c6390508cee1d0277f4712bf01a01a46677233f16387fae072d07bdee4f535b0bd66efa4f2475dc8515696cbc4bc2280c20c93726212695d770b0a8295e2bacbd6b59487b329cc36a5516567b948fed368bf02c50a39e6549312dc6badfef84d4e30494e9ef0a47bd97305639c875b16306fcd91146d3d126c1ea476')
p = int('10541549431842783633587614316112542499895727166990860537947158205451961334065983715903944224868775308489240169949600619123741969714205272515647199022167453')
q = int('11254692541324720060752707148186767582750062945630785066774422168535575089335596479399029695524722638167959390210621853422825328846580189277644256392390351')
n = int('118641897764566817417551054135914458085151243893181692085585606712347004549784923154978949512746946759125187896834583143236980760760749398862405478042140850200893707709475167551056980474794729592748211827841494511437980466936302569013868048998752111754493558258605042130232239629213049847684412075111663446003')

# Calculate the private exponent
phi = (p - 1) * (q - 1)
e = 65537  # This is the standard public exponent for RSA
d = pow(e, -1, phi)

# Create the RSA key
key = RSA.construct((n, e, d))

# Create the cipher and decrypt the ciphertext
cipher = PKCS1_OAEP.new(key)
flag = cipher.decrypt(ct)

print(flag)
```


#### FLAG
```
HTB{v3r1fy1ng_pr1m3s_m0dul0_p0w3rs_0f_10!}
```