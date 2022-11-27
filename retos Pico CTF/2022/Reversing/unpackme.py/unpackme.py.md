
**Descripcion**

Can you get the flag?Reverse engineer this [Python program](https://artifacts.picoctf.net/c/465/unpackme.flag.py).

**Solucion**
```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/unpackme.py]
└─$ ls
unpackme.flag.py  unpackme.py.md
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/unpackme.py]
└─$ file unpackme.flag.py 
unpackme.flag.py: Python script, ASCII text executable, with very long lines (305)
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/unpackme.py]
└─$ cat unpackme.flag.py 
import base64
from cryptography.fernet import Fernet



payload = b'gAAAAABiMD06eCisTWoohiYL5jHGdCte5LAviTFguZQSIyRLAWICJpmdrgxhdTB923h6eksddKpKH41I5-HGzI6xGF_7eb_1u0S2Phw2NvYGTF1KzE1-AU66FfIW6QXWnCpPHOS9CatNBuFXuyjEAx86Rld2E7GjvuKEOJJXx_GZE2JgAxnDmvcewoksfjVCCAwNqzixpUPKkIET2xmO4EsDqK4CUG8_JxP0HwSEzW4PH-hVpZrkyse4EodFPsjs7NVJF0hL1_8bP1TCiEEnFn7hCoTRRvlpYQ=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
exec(plain.decode())
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/unpackme.py]
└─$ nano unpackme.flag.py 
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/unpackme.py]
└─$ nano unpackme.flag.py
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/unpackme.py]
└─$ cat unpackme.flag.py
import base64
from cryptography.fernet import Fernet



payload = b'gAAAAABiMD06eCisTWoohiYL5jHGdCte5LAviTFguZQSIyRLAWICJpmdrgxhdTB923h6eksddKpKH41I5-HGzI6xGF_7eb_1u0S2Phw2NvYGTF1KzE1-AU66FfIW6QXWnCpPHOS9CatNBuFXuyjEAx86Rld2E7GjvuKEOJJXx_GZE2JgAxnDmvcewoksfjVCCAwNqzixpUPKkIET2xmO4EsDqK4CUG8_JxP0HwSEzW4PH-hVpZrkyse4EodFPsjs7NVJF0hL1_8bP1TCiEEnFn7hCoTRRvlpYQ=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
print(plain.decode())
exec(plain.decode())
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/unpackme.py]
└─$ python unpackme.flag.py    

pw = input('What\'s the password? ')

if pw == 'batteryhorse':
  print('picoCTF{175_chr157m45_cd82f94c}')
else:
  print('That password is incorrect.')


What's the password? 
That password is incorrect.
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/unpackme.py]
└─$ 
```
picoCTF{175_chr157m45_cd82f94c}

**Notas Adicionales**