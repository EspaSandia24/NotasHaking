**Solucion**
```bash
──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Crypto/MiniRsa]
└─$ wget https://jupiter.challenges.picoctf.org/static/d21037ad23ed84cfff20a84768a0f2b2/ciphertext
--2022-10-20 09:11:28--  https://jupiter.challenges.picoctf.org/static/d21037ad23ed84cfff20a84768a0f2b2/ciphertext
Resolviendo jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Conectando con jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)[3.131.60.8]:443... conectado.
Petición HTTP enviada, esperando respuesta... 200 OK
Longitud: 884 [application/octet-stream]
Grabando a: «ciphertext»

ciphertext          100%[===================>]     884  --.-KB/s    en 0.006s  

2022-10-20 09:11:29 (148 KB/s) - «ciphertext» guardado [884/884]

                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Crypto/MiniRsa]
└─$ ls 
ciphertext
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Crypto/MiniRsa]
└─$ cat ciphertext  

N: 29331922499794985782735976045591164936683059380558950386560160105740343201513369939006307531165922708949619162698623675349030430859547825708994708321803705309459438099340427770580064400911431856656901982789948285309956111848686906152664473350940486507451771223435835260168971210087470894448460745593956840586530527915802541450092946574694809584880896601317519794442862977471129319781313161842056501715040555964011899589002863730868679527184420789010551475067862907739054966183120621407246398518098981106431219207697870293412176440482900183550467375190239898455201170831410460483829448603477361305838743852756938687673
e: 3

ciphertext (c): 2205316413931134031074603746928247799030155221252519872650073010782049179856976080512716237308882294226369300412719995904064931819531456392957957122459640736424089744772221933500860936331459280832211445548332429338572369823704784625368933 
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Crypto/MiniRsa]
└─$ pip install gmpy2       
Defaulting to user installation because normal site-packages is not writeable
Collecting gmpy2
  Downloading gmpy2-2.1.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.6/3.6 MB 244.2 kB/s eta 0:00:00
Installing collected packages: gmpy2
Successfully installed gmpy2-2.1.2
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Crypto/MiniRsa]
└─$ python3                 
Python 3.10.5 (main, Jun  8 2022, 09:26:22) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from gmpy2 import *
>>> fro Crypto.Util.number import *
  File "<stdin>", line 1
    fro Crypto.Util.number import *
        ^^^^^^
SyntaxError: invalid syntax
>>> from Crypto.Util.number import *
>>> e = 3
>>> c=2205316413931134031074603746928247799030155221252519872650073010782049179856976080512716237308882294226369300412719995904064931819531456392957957122459640736424089744772221933500860936331459280832211445548332429338572369823704784625368933
>>> root, exact = iroot(c,e)
>>> root
mpz(13016382529449106065894479374027604750406953699090365388203708028670029596145277)
>>> exact
True
>>> long_to_byte(root)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'long_to_byte' is not defined. Did you mean: 'long_to_bytes'?
>>> from Crypto.Util.number import long_to_bytes
>>> long_to_bytes(root)
b'picoCTF{n33d_a_lArg3r_e_ccaa7776}'
>>> 


```
picoCTF{n33d_a_lArg3r_e_ccaa7776}