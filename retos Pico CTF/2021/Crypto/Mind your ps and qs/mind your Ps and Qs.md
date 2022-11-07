**Descripcion**

In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? [values](https://mercury.picoctf.net/static/2604f8b51a5cc62d38a3736938f19cef/values)

**Solucion**

```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Crypto/Mind your ps and qs]
└─$ ls 
'mind your Ps and Qs.md'   values
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Crypto/Mind your ps and qs]
└─$ cat values    
Decrypt my super sick RSA:
c: 861270243527190895777142537838333832920579264010533029282104230006461420086153423
n: 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e: 65537                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Crypto/Mind your ps and qs]
└─$ 


```
factorizamos n para sacar p y q
![[Pasted image 20221025081058.png]]
p=1955175890537890492055221842734816092141
q=670577792467509699665091201633524389157003

```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Crypto/Mind your ps and qs]
└─$ python3          
Python 3.10.5 (main, Jun  8 2022, 09:26:22) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
c>>> c=861270243527190895777142537838333832920579264010533029282104230006461420086153423
>>> e=65537
>>> n=1311097532562595991877980619849724606784164430105441327897358800116889057763413423
>>> p=1955175890537890492055221842734816092141
>>> q=670577792467509699665091201633524389157003
>>> tn=(p-1)*(q-1)
>>> form Crypo.Util.number import long_to_bytes
  File "<stdin>", line 1
    form Crypo.Util.number import long_to_bytes
         ^^^^^
SyntaxError: invalid syntax
>>> from Crypo.Util.number import long_to_bytes
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'Crypo'
>>> from Crypto.Util.number import long_to_bytes
>>> from Crypto.Util.number import inverse
>>> d=inverse(e,tn)
>>> d
693529123416505412979446025120625035374876994645029007711823240743237277989774953
>>> m = pow(c,d,n)
>>> m
13016382529449106065927291425342535437996222135352905256639573959002849415739773
>>> long_to_bytes(m)
b'picoCTF{sma11_N_n0_g0od_13686679}'
>>> 

```
**Notas Adicionales**