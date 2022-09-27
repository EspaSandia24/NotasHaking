**Descripcion**

Fix the syntax error in this Python script to print the flag.[Download Python script](https://artifacts.picoctf.net/c/38/fixme1.py)

**Solucion**

descargamos el .py que nos dan y lo ejecutamos nos da error pero con el comando nano lo editamos lo corregimos y ejecutamos de nuevo y nos da la bandera 
```bash
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ python fixme1.py
  File "/home/espasandia24/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022/fixme1.py", line 18
    flag = str_xor(flag_enc, 'enkidu')
IndentationError: unexpected indent
                                                                                                                             
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ nano fixme1.py  
                                                                                                                             
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ python fixme1.py
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_09ee727a}
                                                                                                                             
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ 

```
picoCTF{1nd3nt1ty_cr1515_09ee727a}
**Notas Adicionales**