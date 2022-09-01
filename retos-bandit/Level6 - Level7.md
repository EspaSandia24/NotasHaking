**Bandit **

**Objetivo**
La contraseña para el siguiente nivel se almacena **en algún lugar del servidor** y tiene todas las siguientes propiedades:

-   propiedad del usuario bandit7
-   propiedad del grupo bandit6
-   33 bytes de tamaño

**Datos de acceso**
server: **bandit.labs.overthewire.org** 
usuario: **bandit6*
contraseña: DXjZPULLxYr17uwoI01bNLQbtFemEgo7

**Solucion**
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null/var/lib/dpkg/info/bandit7.password
-bash: /dev/null/var/lib/dpkg/info/bandit7.password: Not a directory
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
bandit6@bandit:~$

**Notas adicionales** 

**Referencias** 