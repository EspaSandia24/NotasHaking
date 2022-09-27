**Descripcion**

Fix the syntax error in the Python script to print the flag.[Download Python script](https://artifacts.picoctf.net/c/67/fixme2.py)

**Solucion**
como en el problema anterior modificamos el .py ya que tenia error con el comando nano para que nos diera la bandera

```bash
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ ls   
 Codebook.md    code.py        convertme.py.md   fixme2.py      fixmel.py.md    'PW Crack 1.md'  'PW Crack 3.md'
 codebook.txt   convertme.py   fixme1.py         fixme2.py.md  'Glitch Cat.md'  'PW Crack 2.md'   runme.py.md
                                                                                                                             
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ python fixme2.py
  File "/home/espasandia24/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022/fixme2.py", line 22
    if flag = "":
       ^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
                                                                                                                             
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ nano fixme2.py
                                                                                                                             
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ python fixme2.py
That is correct! Here's your flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_f6a5aefc}
                                                                                                                             
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ 

```

**Notas Adicionales**