**Descripcion**

Can you find the flag? [shark1.pcapng](https://mercury.picoctf.net/static/81c7862241faf4a48bd64a858392c92b/shark1.pcapng).

**Solucion**
```
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/wireshark doo dooo do doo]
└─$ wget https://mercury.picoctf.net/static/81c7862241faf4a48bd64a858392c92b/shark1.pcapng
--2022-11-09 13:51:30--  https://mercury.picoctf.net/static/81c7862241faf4a48bd64a858392c92b/shark1.pcapng
Resolviendo mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Conectando con mercury.picoctf.net (mercury.picoctf.net)[18.189.209.142]:443... conectado.
Petición HTTP enviada, esperando respuesta... 200 OK
Longitud: 1558808 (1.5M) [application/octet-stream]
Grabando a: «shark1.pcapng»

shark1.pcapng       100%[===================>]   1.49M   292KB/s    en 5.2s    

2022-11-09 13:51:36 (292 KB/s) - «shark1.pcapng» guardado [1558808/1558808]

                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/wireshark doo dooo do doo]
└─$ ls 
shark1.pcapng  Untitled.md
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/wireshark doo dooo do doo]
└─$ open shark1.pcapng 
```

revisamos los paquetes hasta encontrar algo parecido a la bandera 

![[Pasted image 20221109140906.png]]

cvpbPGS{c33xno00_1_f33_h_qrnqorrs}
a esta le aplicamos un rot 13 para que nos de la vandera como es 
![[Pasted image 20221109141547.png]]
picoCTF{p33kab00_1_s33_u_deadbeef}

**Notas Adicionales**