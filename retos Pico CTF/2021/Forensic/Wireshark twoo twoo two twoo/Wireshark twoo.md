**Descripcion**



**Solucion**
```bash
 ┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Wireshark twoo twoo two twoo]
└─$ ls                                          
shark1.pcapng  shark2.pcapng  Untitled.md
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Wireshark twoo twoo two twoo]
└─$ file shark2.pcapng                          
shark2.pcapng: pcapng capture file - version 1.0

┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Wireshark twoo twoo two twoo]
└─$ open shark2.pcapng 
```
![[shark.png]]
![[shark 1.png]]
![[shark 2.png]]
lo exportamos 

```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Wireshark twoo twoo two twoo]
└─$ ls                         
bandera.csv  shark1.pcapng  shark2.pcapng  Untitled.md
                                                                                                  
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Wireshark twoo twoo two twoo]
└─$ cat bandera.csv  
"No.","Time","Source","Destination","Protocol","Length","Info"
"1637","9.440363","192.168.38.104","18.217.1.57","DNS","109","Standard query 0x1dd2 A cGljb0NU.reddshrimpandherring.com.windomain.local"
"2046","11.972605","192.168.38.104","18.217.1.57","DNS","109","Standard query 0xabb9 A RntkbnNf.reddshrimpandherring.com.windomain.local"
"2448","14.605726","192.168.38.104","18.217.1.57","DNS","109","Standard query 0x9e21 A M3hmMWxf.reddshrimpandherring.com.windomain.local"
"3153","16.506492","192.168.38.104","18.217.1.57","DNS","109","Standard query 0x2ee1 A ZnR3X2Rl.reddshrimpandherring.com.windomain.local"
"3442","18.340155","192.168.38.104","18.217.1.57","DNS","109","Standard query 0x2a4b A YWRiZWVm.reddshrimpandherring.com.windomain.local"
"3982","20.369626","192.168.38.104","18.217.1.57","DNS","105","Standard query 0x4068 A fQ==.reddshrimpandherring.com.windomain.local"
"4374","22.583745","192.168.38.104","18.217.1.57","DNS","105","Standard query 0x7418 A fQ==.reddshrimpandherring.com.windomain.local"
                                                                                                  
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Wireshark twoo twoo two twoo]
└─$ nano bandera.csv 
                                                                                                  
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Wireshark twoo twoo two twoo]
└─$ cat bandera.csv | cut -d "," -f 7 | cut -d " " -f 5
cGljb0NU.reddshrimpandherring.com.windomain.local"
RntkbnNf.reddshrimpandherring.com.windomain.local"
M3hmMWxf.reddshrimpandherring.com.windomain.local"
ZnR3X2Rl.reddshrimpandherring.com.windomain.local"
YWRiZWVm.reddshrimpandherring.com.windomain.local"
fQ==.reddshrimpandherring.com.windomain.local"

                                                                                                  
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Wireshark twoo twoo two twoo]
└─$ cat bandera.csv | cut -d "," -f 7 | cut -d " " -f 5| cut -d "." -f1 
cGljb0NU
RntkbnNf
M3hmMWxf
ZnR3X2Rl
YWRiZWVm
fQ==

                                                                                                  
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Wireshark twoo twoo two twoo]
└─$ cat bandera.csv | cut -d "," -f 7 | cut -d " " -f 5| cut -d "." -f1 | base64 -d
picoCTF{dns_3xf1l_ftw_deadbeef}                                                                                                  
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Wireshark twoo twoo two twoo]
└─$ 

```
picoCTF{dns_3xf1l_ftw_deadbeef}
**Notas Adicionales**