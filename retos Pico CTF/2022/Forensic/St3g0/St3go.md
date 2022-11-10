**Descripcion**

Download this image and find the flag.

-   [Download image](https://artifacts.picoctf.net/c/422/pico.flag.png)

**Solucion**
```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/St3g0]
└─$ wget https://artifacts.picoctf.net/c/422/pico.flag.png                    
--2022-11-10 09:15:48--  https://artifacts.picoctf.net/c/422/pico.flag.png
Resolviendo artifacts.picoctf.net (artifacts.picoctf.net)... 54.230.21.115, 54.230.21.83, 54.230.21.88, ...
Conectando con artifacts.picoctf.net (artifacts.picoctf.net)[54.230.21.115]:443... conectado.
Petición HTTP enviada, esperando respuesta... 200 OK
Longitud: 13441 (13K) [application/octet-stream]
Grabando a: «pico.flag.png»

pico.flag.png       100%[===================>]  13.13K  64.6KB/s    en 0.2s    

2022-11-10 09:15:58 (64.6 KB/s) - «pico.flag.png» guardado [13441/13441]

                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/St3g0]
└─$ ls 
pico.flag.png  St3go.md
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/St3g0]
└─$ zsteg .a -v pico.flag.png 
zsteg: command not found
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/St3g0]
└─$ zsteg -a -v pico.flag.png
zsteg: command not found
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/St3g0]
└─$ sudo gem install zsteg            
[sudo] contraseña para espasandia24: 
Fetching zsteg-0.2.11.gem
Fetching zpng-0.4.3.gem
Fetching rainbow-3.1.1.gem
Fetching iostruct-0.0.4.gem
Successfully installed rainbow-3.1.1
Successfully installed zpng-0.4.3
Successfully installed iostruct-0.0.4
Successfully installed zsteg-0.2.11
Parsing documentation for rainbow-3.1.1
Installing ri documentation for rainbow-3.1.1
Parsing documentation for zpng-0.4.3
Installing ri documentation for zpng-0.4.3
Parsing documentation for iostruct-0.0.4
Installing ri documentation for iostruct-0.0.4
Parsing documentation for zsteg-0.2.11
Installing ri documentation for zsteg-0.2.11
Done installing documentation for rainbow, zpng, iostruct, zsteg after 8 seconds
4 gems installed
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/St3g0]
└─$ zsteg -a -v pico.flag.png
b1,rgb,lsb,xy       .. text: "picoCTF{7h3r3_15_n0_5p00n_a1062667}$t3g0"
    00000000: 70 69 63 6f 43 54 46 7b  37 68 33 72 33 5f 31 35  |picoCTF{7h3r3_15|
    00000010: 5f 6e 30 5f 35 70 30 30  6e 5f 61 31 30 36 32 36  |_n0_5p00n_a10626|
    00000020: 36 37 7d 24 74 33 67 30  00 00 00 00 00 00 00 00  |67}$t3g0........|
    00000030: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
    *
    000000f0: 00 00 00 00 01 42 f3 6d  b6 db 6d b6 db 6d b6 db  |.....B.m..m..m..|
b1,abgr,lsb,xy      .. text: "E2A5q4E%uSA"
    00000000: 61 03 15 16 66 31 45 21  24 17 51 37 62 06 45 32  |a...f1E!$.Q7b.E2|
    00000010: 41 35 71 34 45 25 75 53  41 05 71 35 61 06 00 30  |A5q4E%uSA.q5a..0|
    00000020: 66 15 75 14 41 a6 00 3b  49 96 60 b3 4d b7 b1 99  |f.u.A..;I.`.M...|
    00000030: ed 06 45 17 41    
```
picoCTF{7h3r3_15_n0_5p00n_a1062667}
**Notas Adicionales**