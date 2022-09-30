**Descripcion**

Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/17/level2.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/17/level2.flag.txt.enc) in the same directory too.

**Solucion**
leemos el .py donde podemos ver que viene la contraseña  pero no viene como tal entonces usamos python para poder imprimirla 
```Bash
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ python level2.py  
Please enter correct password for flag: ksjs
That password is incorrect
                                                                                
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ cat level2.flag.txt.enc 
D
 Vw1%B@W
        \:ZRWS:ZT
                 T                                                                                
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ cat level2.py          
### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('level2.flag.txt.enc', 'rb').read()



def level_2_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39) ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_2_pw_check()
                                                                                
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ python            
Python 3.10.5 (main, Jun  8 2022, 09:26:22) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print(chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39))
4ec9
>>> exit()
                                                                                
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ python level2.py 
Please enter correct password for flag: 4ec9
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_9701e681}
                                                                                
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ 

```
picoCTF{tr45h_51ng1ng_9701e681}
**Notas Adicionales**