# Variables and more variables
## Descripciòn
Considere un sistema RSA con p=7, q= 11 y e=13, encuentre el texto plano correspondiente a c=17. Encuentra el valor de m.

## Soluciòn
```python
┌──(kali㉿kali)-[~]
└─$ python
>>> p=7
>>> q=11
>>> e=13
>>> c=17
>>> n=p*q
>>> n
77
>>> from Crypto.Util.number import inverse
>>> d=inverse(e,tn)
>>> d
37
>>> m=pow(c,d,n)
>>> m
52
```


**Flag:** 

## Referencias
- []()