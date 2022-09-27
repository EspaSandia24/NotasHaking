**Descripcion**

Our flag printing service has started glitching!`$ nc saturn.picoctf.net 53933`

**Solucion**
ejecutamos python para imprimir los que nos da ala hora de entrar al servidor

```bash
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/Examen pico CFT/Beginner PicoMIni 2022]
└─$ python
Python 3.10.5 (main, Jun  8 2022, 09:26:22) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print('picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}')
picoCTF{gl17ch_m3_n07_a4392d2e}
>>> 
KeyboardInterrupt
>>> 


```
picoCTF{gl17ch_m3_n07_a4392d2e
**Notas Adicionales**