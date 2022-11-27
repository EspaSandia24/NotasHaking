**Descripcion**

Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"?Download the program [here](https://artifacts.picoctf.net/c/352/run).

**Solucion**
```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/file-run2]
└─$ ls
'file run 2.md'   run
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/file-run2]
└─$ file run       
run: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=689b8959bc0a65415698970bbb93ed2788442ffb, for GNU/Linux 3.2.0, not stripped
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/file-run2]
└─$ ./run
Run this file with only one argument.
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/file-run2]
└─$ ./run test
Won't you say 'Hello!' to me first?
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/file-run2]
└─$ ./run Hello!
The flag is: picoCTF{F1r57_4rgum3n7_96f2195f}                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/file-run2]
└─$ 
```

picoCTF{F1r57_4rgum3n7_96f2195f}

**Notas Adicionales**