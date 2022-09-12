**Bandit **

**Objetivo**
¡Buen trabajo consiguiendo una concha! ¡Ahora date prisa y obtén la contraseña para bandit27!

**Datos de acceso**
server: **bandit.labs.overthewire.org** 
usuario: **bandit19**
contraseña: c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1
**Solucion**
```bash
se hace chiquita la pantalla
y se pone :set shell=/bin/bash
y luego shell

:shell
bandit26@bandit:~$ ls -la
total 44                                                                             
drwxr-xr-x  3 root     root      4096 Sep  1 06:30 .
drwxr-xr-x 49 root     root      4096 Sep  1 06:30 ..                                
-rwsr-x---  1 bandit27 bandit26 14872 Sep  1 06:30 bandit27-do
-rw-r--r--  1 root     root       220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root     root      3771 Jan  6  2022 .bashrc
-rw-r--r--  1 root     root       807 Jan  6  2022 .profile
drwxr-xr-x  2 root     root      4096 Sep  1 06:30 .ssh
-rw-r-----  1 bandit26 bandit26   258 Sep  1 06:30 text.txt
bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27
YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS
bandit26@bandit:~$  
```
**Notas adicionales** 

**Referencias** 