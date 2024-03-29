# Primary Knowledge
* **Event:** Cyber Apocalypse 2024
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Very Easy

## Description
Surrounded by an untamed forest and the serene waters of the Primus river, your sole objective is surviving for 24 hours. Yet, survival is far from guaranteed as the area is full of Rattlesnakes, Spiders and Alligators and the weather fluctuates unpredictably, shifting from scorching heat to torrential downpours with each passing hour. Threat is compounded by the existence of a virtual circle which shrinks every minute that passes. Anything caught beyond its bounds, is consumed by flames, leaving only ashes in its wake. As the time sleeps away, you need to prioritise your actions secure your surviving tools. Every decision becomes a matter of life and death. Will you focus on securing a shelter to sleep, protect yourself against the dangers of the wilderness, or seek out means of navigating the Primus’ waters?


## Steps
#### Step 1
This RSA challenge involves a prime number n that is not a product of two primes, but is prime itself. So, in this situation we take phi as n-1.

## Code
```python
from Crypto.Util.number import inverse , long_to_bytes

c = 15114190905253542247495696649766224943647565245575793033722173362381895081574269185793855569028304967185492350704248662115269163914175084627211079781200695659317523835901228170250632843476020488370822347715086086989906717932813405479321939826364601353394090531331666739056025477042690259429336665430591623215 
e = 0x10001      
n = 144595784022187052238125262458232959109987136704231245881870735843030914418780422519197073054193003090872912033596512666042758783502695953159051463566278382720140120749528617388336646147072604310690631290350467553484062369903150007357049541933018919332888376075574412714397536728967816658337874664379646535347  

# Compute Euler's totient function phi(n) = n - 1 since n is prime
phi_n = n - 1

d = inverse(e, phi_n)

m = pow(c, d, n)

print("Decrypted message:", m)
print(long_to_bytes(m))

```


#### FLAG
```
HTB{0h_d4mn_4ny7h1ng_r41s3d_t0_0_1s_1!!!}
```