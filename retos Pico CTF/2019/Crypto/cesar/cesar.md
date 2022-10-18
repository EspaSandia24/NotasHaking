```
┌──(espasandia24㉿kali)-[~/…/HakinKali/retos Pico CTF/2019/Crypto]
└─$ mkdir cesar   
                                                                                
┌──(espasandia24㉿kali)-[~/…/HakinKali/retos Pico CTF/2019/Crypto]
└─$ cd cesar  
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Crypto/cesar]
└─$ wget https://jupiter.challenges.picoctf.org/static/6385b895dcb30c74dbd1f0ea271e3563/ciphertext  
--2022-10-18 08:30:24--  https://jupiter.challenges.picoctf.org/static/6385b895dcb30c74dbd1f0ea271e3563/ciphertext
Resolviendo jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Conectando con jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)[3.131.60.8]:443... conectado.
Petición HTTP enviada, esperando respuesta... 200 OK
Longitud: 35 [application/octet-stream]
Grabando a: «ciphertext»

ciphertext          100%[===================>]      35  --.-KB/s    en 0s      

2022-10-18 08:30:26 (12.4 MB/s) - «ciphertext» guardado [35/35]

                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Crypto/cesar]
└─$ ls
ciphertext
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Crypto/cesar]
└─$ cat ciphertext  
picoCTF{dspttjohuifsvcjdpoabrkttds}                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Crypto/cesar]
└─$ nano cesarr.py
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Crypto/cesar]
└─$ python3  cesarr.py 
  File "/home/espasandia24/Escritorio/HakinKali/retos Pico CTF/2019/Crypto/cesar/cesarr.py", line 9
    flag += letras[(letras.find(c)+rot)%26]
    ^
IndentationError: expected an indented block after 'for' statement on line 8
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Crypto/cesar]
└─$ nano cesarr.py
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Crypto/cesar]
└─$ python3  cesarr.py
crossingtherubiconzaqjsscr
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Crypto/cesar]
└─$ 

```

picoCTF{crossingtherubiconzaqjsscr}