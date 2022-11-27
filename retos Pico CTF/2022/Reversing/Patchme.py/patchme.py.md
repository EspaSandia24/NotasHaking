**Descripcion**

Can you get the flag?Run this [Python program](https://artifacts.picoctf.net/c/387/patchme.flag.py) in the same directory as this [encrypted flag](https://artifacts.picoctf.net/c/387/flag.txt.enc).

**Solucion**
```bash
┌──(espasandia24㉿kali)-[~/…/HakinKali/retos Pico CTF/2022/Reversing]
└─$ cd Patchme.py 
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/Patchme.py]
└─$ ls
flag.txt.enc  patchme.flag.py  patchme.py.md
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/Patchme.py]
└─$ cat flag.txt.enc 

CR1@    UYX+
6QC

                                                                                   
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/Patchme.py]
└─$ cat patchme.flag.py 
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


flag_enc = open('flag.txt.enc', 'rb').read()



def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "ak98" + \
                   "-=90" + \
                   "adfjhgj321" + \
                   "sleuth9000"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), "utilitarian")
        print(decryption)
        return
    print("That password is incorrect")



level_1_pw_check()
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/Patchme.py]
└─$ python3 patchme.flag.py    
Please enter correct password for flag: nk
That password is incorrect
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/Patchme.py]
└─$ nano patchme.flag.py 
```
modificamos el .py para que no valide la vandera y asi al ejecutarlo nos da la bandera
![[Pasted image 20221126140022.png]]

```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/Patchme.py]
└─$ nano patchme.flag.py   
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/Patchme.py]
└─$ python3 patchme.flag.py
Please enter correct password for flag: 
Welcome back... your flag, user:
picoCTF{p47ch1ng_l1f3_h4ck_f01eabfa}
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/Patchme.py]
└─$ 
```

picoCTF{p47ch1ng_l1f3_h4ck_f01eabfa}

**Notas Adicionales**