**Descripcion**

Can you get the flag?Download this [binary](https://artifacts.picoctf.net/c/116/gdbme).Here's the test drive instructions:

-   `$ chmod +x gdbme`
-   `$ gdb gdbme`
-   `(gdb) layout asm`
-   `(gdb) break *(main+99)`
-   `(gdb) run`
-   `(gdb) jump *(main+104)`

**Solucion**
```bash
┌──(espasandia24㉿kali)-[~/…/HakinKali/retos Pico CTF/2022/Reversing]
└─$ ls
bloat.py   file-run2       Patchme.py   unpackme.py
file-run1  GDB-Test-Drive  Safe-Opener
                                                                                
┌──(espasandia24㉿kali)-[~/…/HakinKali/retos Pico CTF/2022/Reversing]
└─$ cd GDB-Test-Drive 
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/GDB-Test-Drive]
└─$ ls
'GDB test drive.md'   gdbme
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/GDB-Test-Drive]
└─$ file gdbme 
gdbme: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=4a97837ebdcca2413f854f9274b4dc31f16f2aee, for GNU/Linux 3.2.0, not stripped
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/GDB-Test-Drive]
└─$ 
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/GDB-Test-Drive]
└─$ chmod +x gdbme   
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/GDB-Test-Drive]
└─$ ls
'GDB test drive.md'   gdbme
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/GDB-Test-Drive]
└─$ ./gdbme     
hola 
sls
^C
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/GDB-Test-Drive]
└─$ gdb gd             
Command 'gdb' not found, but can be installed with:
sudo apt install gdb        
sudo apt install gdb-minimal
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/GDB-Test-Drive]
└─$ 

```


**Notas Adicionales**