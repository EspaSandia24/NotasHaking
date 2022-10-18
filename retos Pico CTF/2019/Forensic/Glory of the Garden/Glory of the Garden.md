**Descripcion**

This [garden](https://jupiter.challenges.picoctf.org/static/43c4743b3946f427e883f6b286f47467/garden.jpg) contains more than it seems.

**Solucion**
``` bash

┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/Glory of the Garden]
└─$ ls 
 garden.jpg  'Glory of the Garden.md'
                                                                                                                       
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/Glory of the Garden]
└─$  file garden.jpg 
garden.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, baseline, precisio 2999x2249, components 3
                                                                                                                       
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/Glory of the Garden]
└─$ open garden.jpg   
                                                                                                                       
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/Glory of the Garden]
└─$ hexeditor garden.jpg
```
![[Pasted image 20221016141027.png]]
![[Pasted image 20221016141113.png]]
![[Pasted image 20221016140644.png]]
picoCTF{more_than_m33ts_the_3y3657BaB2C}
**Notas Adicionales**