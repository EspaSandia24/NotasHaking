**Descripcion
**
Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it. Download the data [here](https://artifacts.picoctf.net/c/295/anthem.flag.txt).

**Solucion**
```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Lookey]
└─$ wget https://artifacts.picoctf.net/c/295/anthem.flag.txt 
--2022-11-10 08:52:40--  https://artifacts.picoctf.net/c/295/anthem.flag.txt
Resolviendo artifacts.picoctf.net (artifacts.picoctf.net)... 54.230.21.115, 54.230.21.83, 54.230.21.23, ...
Conectando con artifacts.picoctf.net (artifacts.picoctf.net)[54.230.21.115]:443... conectado.
Petición HTTP enviada, esperando respuesta... 200 OK
Longitud: 108668 (106K) [application/octet-stream]
Grabando a: «anthem.flag.txt»

anthem.flag.txt     100%[===================>] 106.12K   569KB/s    en 0.2s    

2022-11-10 08:52:49 (569 KB/s) - «anthem.flag.txt» guardado [108668/108668]

                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Lookey]
└─$ ls
 anthem.flag.txt  'Lookey here.md'
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Lookey]
└─$ file anthem.flag.txt       
anthem.flag.txt: Unicode text, UTF-8 text
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Lookey]
└─$ wc -w anthem.flag.txt                                   
19139 anthem.flag.txt
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Lookey]
└─$ cat anthem.flag.txt | grep "picoCTF"
      we think that the men of picoCTF{gr3p_15_@w3s0m3_58f5c024}
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Lookey]
└─$ 


```
picoCTF{gr3p_15_@w3s0m3_58f5c024}
**Notas Adicionales**