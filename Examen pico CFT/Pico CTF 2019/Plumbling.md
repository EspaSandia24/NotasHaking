**Descripcion**

Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to `jupiter.challenges.picoctf.org 7480`.

**Solucion**
 tenemos que acceder al servidor donde esta la bandera pero dentro del servidor hay mas cosas por lo que usamos tambien el comando grep haci haciendo que nos de directamente la bandera 
```bash
┌──(espasandia24㉿kali)-[~]
└─$ nc jupiter.challenges.picoctf.org 7480 | grep pico
picoCTF{digital_plumb3r_06e9d954}
                                                                             
┌──(espasandia24㉿kali)-[~]
└─$ 

```
picoCTF{digital_plumb3r_06e9d954}
**Notas Adicionales**