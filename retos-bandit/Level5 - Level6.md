**Bandit **

**Objetivo**
La contraseña para el siguiente nivel se almacena en un archivo en algún lugar del directorio **inhere** y tiene todas las siguientes propiedades:v

**Datos de acceso**
server: **bandit.labs.overthewire.org** 
usuario: **bandit5**
contraseña: koReBOKuIDDepwhWk7jZC0RTdopnAYKh
**Solucion**
```bash
bandit5@bandit:~/inhere$ find . -type f size 1033c
find: paths must precede expression: size
Try 'find --help' for more information.
bandit5@bandit:~/inhere$ find . -type f -size 1033c
./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```

**Notas adicionales** 

**Referencias** 
