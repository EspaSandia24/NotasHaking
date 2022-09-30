**Descripcion**

Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/24/level3.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/24/level3.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/24/level3.hash.bin) in the same directory too.There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

**Solucion**

en este caso es casi como el 1 y 2, con la diferencia de que estaves en el .py  se ecuentran varias contraseñas por locual tenemos que intentarle con esas hasta que le demos a la correcta
```bash
                                                                                
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ ls
 Codebook.md       fixme1.py.md          level2.flag.txt.enc  'PW Crack 2.md'
 codebook.txt      fixme2.py             level2.py            'PW Crack 3.md'
 code.py           fixme2.py.md          level3.flag.txt.enc   runme.py
 convertme.py     'Glitch Cat.md'        level3.hash.bin       runme.py.md
 convertme.py.md   level1.flag.txt.enc   level3.py
 fixme1.py         level1.py            'PW Crack 1.md'
                                                                                
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ cat level3.py
import hashlib

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

flag_enc = open('level3.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level3.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_3_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_3_pw_check()


# The strings below are 7 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]

                                                                                
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ python level3.py 
Please enter correct password for flag: f09e
That password is incorrect
                                                                                
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ python level3.py 
Please enter correct password for flag: 4dcf
That password is incorrect                                                       
                                                                                 
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ python level3.py 
Please enter correct password for flag: 87ab
That password is incorrect
                                                                                 
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ python level3.py 
Please enter correct password for flag: dba8
Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_cd6ed2eb}
                                                                                 
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ 

```
picoCTF{m45h_fl1ng1ng_cd6ed2eb}

**Notas Adicionales**