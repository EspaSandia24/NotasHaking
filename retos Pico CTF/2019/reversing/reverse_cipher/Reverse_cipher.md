**Descripcion**

We have recovered a [binary](https://jupiter.challenges.picoctf.org/static/31c9b832d036a10daeef52d8b4290ef0/rev) and a [text file](https://jupiter.challenges.picoctf.org/static/31c9b832d036a10daeef52d8b4290ef0/rev_this). Can you reverse the flag.

**Solucion**

```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/reverse_cipher]
└─$ wget https://jupiter.challenges.picoctf.org/static/31c9b832d036a10daeef52d8b4290ef0/rev            
--2022-11-19 15:09:32--  https://jupiter.challenges.picoctf.org/static/31c9b832d036a10daeef52d8b4290ef0/rev
Resolviendo jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Conectando con jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)[3.131.60.8]:443... conectado.
Petición HTTP enviada, esperando respuesta... 200 OK
Longitud: 16856 (16K) [application/octet-stream]
Grabando a: «rev»

rev                 100%[===================>]  16.46K  --.-KB/s    en 0.05s   

2022-11-19 15:09:33 (307 KB/s) - «rev» guardado [16856/16856]

                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/reverse_cipher]
└─$ wget https://jupiter.challenges.picoctf.org/static/31c9b832d036a10daeef52d8b4290ef0/rev_this
--2022-11-19 15:09:56--  https://jupiter.challenges.picoctf.org/static/31c9b832d036a10daeef52d8b4290ef0/rev_this
Resolviendo jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Conectando con jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)[3.131.60.8]:443... conectado.
Petición HTTP enviada, esperando respuesta... 200 OK
Longitud: 24 [application/octet-stream]
Grabando a: «rev_this»

rev_this            100%[===================>]      24  --.-KB/s    en 0s      

2022-11-19 15:09:56 (9.21 MB/s) - «rev_this» guardado [24/24]

                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/reverse_cipher]
└─$ ls 
rev  rev_this
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/reverse_cipher]
└─$ ls -la                            
total 25
drwxrwx--- 1 root vboxsf     0 nov 19 15:12 .
drwxrwx--- 1 root vboxsf  4096 nov 16 17:54 ..
-rwxrwx--- 1 root vboxsf 16856 oct 26  2020 rev
-rwxrwx--- 1 root vboxsf   314 nov 19 15:13 Reverse_cipher.md
-rwxrwx--- 1 root vboxsf    24 oct 26  2020 rev_this
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/reverse_cipher]
└─$ file rev            
rev: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=523d51973c11197605c76f84d4afb0fe9e59338c, not stripped
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/reverse_cipher]
└─$ file rev_this 
rev_this: ASCII text, with no line terminators
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/reverse_cipher]
└─$ cat rev_this 
picoCTF{w1{1wq85jc=2i0<}                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/reverse_cipher]
└─$ cat rev |wc 
      5      75   16856
 

```

**Notas Adicionales**