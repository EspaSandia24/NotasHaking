# General
## Objetivo
help us review this code in this [file](https://drive.google.com/file/d/1gLEsMvKICvOyu1DsnKGLiKWujdbgYeIz/view?usp=sharing)
## Pistas
## Solucion
┌─[✗]─[oscar@oscar-parrot]─[~/Metaredperu/General/BadCode]
└──╼ $nano badcode.py 

El error se encuentra en la identacion del return, se recorre la linea un espacio y se corrije 
tambien la variable 
flag_enc
contiene una " , " de mas al final, se borra


import random



def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])


flag_enc = chr(0x01) + chr(0x21) + chr(0x08) + chr(0x19) + chr(0x21) + chr(0x51) + chr(0x5c) + chr(0x40) + chr(0x3a) + chr(0x24) + chr(0x5d) + chr(0x21) + chr(0x20) + chr(0x07) + chr(0x0a) + chr(0x04)

  
flag = str_xor(flag_enc, 'enkidu')
print('That is correct! Here\'s your flag: ' + flag)



┌─[oscar@oscar-parrot]─[~/Metaredperu/General/BadCode]
└──╼ $python badcode.py 
That is correct! Here's your flag: dOcpE$9.QM9TEiam
┌─[oscar@oscar-parrot]─[~/Metaredperu/General/BadCode]
└──╼ $

## Notas Adicionales
## Referencias