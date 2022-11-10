**Descripcion**

Download the packet capture file and use packet analysis software to find the flag.

-   [Download packet capture](https://artifacts.picoctf.net/c/200/network-dump.flag.pcap)

**Solucion**
```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Packets Primer]
└─$ wget https://artifacts.picoctf.net/c/200/network-dump.flag.pcap
--2022-11-10 08:56:30--  https://artifacts.picoctf.net/c/200/network-dump.flag.pcap
Resolviendo artifacts.picoctf.net (artifacts.picoctf.net)... 54.230.21.88, 54.230.21.23, 54.230.21.83, ...
Conectando con artifacts.picoctf.net (artifacts.picoctf.net)[54.230.21.88]:443... conectado.
Petición HTTP enviada, esperando respuesta... 200 OK
Longitud: 778 [application/octet-stream]
Grabando a: «network-dump.flag.pcap»

network-dump.flag.p 100%[===================>]     778  --.-KB/s    en 0.005s  

2022-11-10 08:56:39 (146 KB/s) - «network-dump.flag.pcap» guardado [778/778]

                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Packets Primer]
└─$ ls 
 network-dump.flag.pcap  'Packets Primer.md'
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Packets Primer]
└─$ wireshark network-dump.flag.pcap
```
![[Pasted image 20221110090206.png]]
![[Pasted image 20221110090139.png]]

picoCTF{p4ck37_5h4rk_b9d53765}
**Notas Adicionales**