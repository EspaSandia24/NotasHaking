Bandit 

Objetivo
The password for the next level is stored in a hidden file in the **inhere** directory.

Datos de acceso
server: **bandit.labs.overthewire.org** 
usuario: **bandit3**
contraseña: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

Solucion

bandit3@bandit:~$ cd inhere/
bandit3@bandit:~/inhere$ ls -a
.  ..  .hidden
bandit3@bandit:~/inhere$ cat .hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
bandit3@bandit:~/inhere$

Notas adicionales 
-a es para poder ver los archivos ocultos

Referencias 