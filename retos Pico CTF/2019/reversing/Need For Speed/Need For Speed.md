**Descripcion**

The name of the game is [speed](https://www.youtube.com/watch?v=8piqd2BWeGI). Are you quick enough to solve this problem and keep it above 50 mph? [need-for-speed](https://jupiter.challenges.picoctf.org/static/cd51b2c95be9f3626db6fe6665afb5a3/need-for-speed).

**Solucion**

```bash
──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/Need For Speed]
└─$ ls 
'Need For Speed.md'   need-for-speed
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/Need For Speed]
└─$ file need-for-speed        
need-for-speed: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=6f1b99bffb980c293d03dd73bd458e6747c3c936, not stripped
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/Need For Speed]
└─$ chmod -x need-for-speed 
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/Need For Speed]
└─$ ./need-for-speed                        
Keep this thing over 50 mph!
============================

Creating key...
Not fast enough. BOOM!
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/Need For Speed]
└─$ objdump -D need-for-speed -M intel | grep '<main>:' -A20
000000000000091a <main>:
 91a:   55                      push   rbp
 91b:   48 89 e5                mov    rbp,rsp
 91e:   48 83 ec 10             sub    rsp,0x10
 922:   89 7d fc                mov    DWORD PTR [rbp-0x4],edi
 925:   48 89 75 f0             mov    QWORD PTR [rbp-0x10],rsi
 929:   b8 00 00 00 00          mov    eax,0x0
 92e:   e8 a5 ff ff ff          call   8d8 <header>
 933:   b8 00 00 00 00          mov    eax,0x0
 938:   e8 f2 fe ff ff          call   82f <set_timer>
 93d:   b8 00 00 00 00          mov    eax,0x0
 942:   e8 36 ff ff ff          call   87d <get_key>
 947:   b8 00 00 00 00          mov    eax,0x0
 94c:   e8 5b ff ff ff          call   8ac <print_flag>
 951:   b8 00 00 00 00          mov    eax,0x0
 956:   c9                      leave
 957:   c3                      ret
 958:   0f 1f 84 00 00 00 00    nop    DWORD PTR [rax+rax*1+0x0]
 95f:   00 

0000000000000960 <__libc_csu_init>:
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/Need For Speed]
└─$ gdb                
Command 'gdb' not found, but can be installed with:
sudo apt install gdb        
sudo apt install gdb-minimal
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/Need For Speed]
└─$ sudo apt install gdb   
[sudo] contraseña para espasandia24: 
Leyendo lista de paquetes... Hecho
Creando árbol de dependencias... Hecho
Leyendo la información de estado... Hecho
Tal vez quiera ejecutar «apt --fix-broken install» para corregirlo.
Los siguientes paquetes tienen dependencias incumplidas:
 gdb : Depende: libbabeltrace1 (>= 1.5.4) pero no va a instalarse
       Depende: libdebuginfod1 (>= 0.180) pero no va a instalarse
       Depende: libipt2 (>= 2.0) pero no va a instalarse
       Depende: libsource-highlight4v5 (>= 3.1.9) pero no va a instalarse
       Recomienda: libc-dbg
 mariadb-server-10.6 : Depende: mariadb-client-10.6 (>= 1:10.6.9-1) pero 1:10.6.8-1 va a ser instalado
                       Depende: mariadb-server-core-10.6 (>= 1:10.6.9-1) pero 1:10.6.8-1 va a ser instalado
 steghide : Depende: libmcrypt4 pero no va a instalarse
            Depende: libmhash2 pero no va a instalarse
E: Dependencias incumplidas. Intente «apt --fix-broken install» sin paquetes (o especifique una solución).
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/Need For Speed]
└─$ 

```
picoCTF{Good job keeping bus #24c43740 speeding along!}
**Notas Adicionales**