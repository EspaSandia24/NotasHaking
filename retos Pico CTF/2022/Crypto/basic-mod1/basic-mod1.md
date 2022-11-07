**Descripcion**

We found this weird message being passed around on the servers, we think we have a working decryption scheme. Download the message [here](https://artifacts.picoctf.net/c/395/message.txt). Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

**Solucion**
```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Crypto/basic-mod1]
└─$ ls
basic-mod1.md  message.txt
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Crypto/basic-mod1]
└─$ cat message.txt 
91 322 57 124 40 406 272 147 239 285 353 272 77 110 296 262 299 323 255 337 150 102                                                                                 
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Crypto/basic-mod1]
└─$ nano descrip.py             
                  
```
![[Pasted image 20221027082222.png]]

```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Crypto/basic-mod1]
└─$ python3 descrip.py 
R0UND_N_R0UND_ADD17EC2

```
picoCTF{R0UND_N_R0UND_ADD17EC2}
**Notas Adicionales**