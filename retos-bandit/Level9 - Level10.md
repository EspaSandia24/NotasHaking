**Bandit **

**Objetivo**
La contraseña para el siguiente nivel se almacena en el archivo **data.txt** en una de las pocas cadenas legibles por humanos, precedida por varios caracteres '='.

**Datos de acceso**
server: **bandit.labs.overthewire.org** 
usuario: **bandit9**
contraseña: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
**Solucion**
bandit9@bandit:~$ strings data.txt | grep ==
========== the*2i"4
========== password
Z)========== is
&========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
bandit9@bandit:~$
**Notas adicionales** 

**Referencias** 