**Bandit **

**Objetivo**

**Datos de acceso**
server: **bandit.labs.overthewire.org** 
usuario: **bandit19**
contraceña: VxCazJaVykI6W36BkBU0mJTCM8rR95XT
**Solucion**
bandit20@bandit:~$ ls -la
total 36
drwxr-xr-x  2 root     root      4096 Sep  1 06:30 .
drwxr-xr-x 49 root     root      4096 Sep  1 06:30 ..
-rw-r--r--  1 root     root       220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root     root      3771 Jan  6  2022 .bashrc
-rw-r--r--  1 root     root       807 Jan  6  2022 .profile
-rwsr-x---  1 bandit21 bandit20 15596 Sep  1 06:30 suconnect
bandit20@bandit:~$ nc localhost 3030
bandit20@bandit:~$ nc -lvp 4020 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT &
[1] 635162
bandit20@bandit:~$ Listening on 0.0.0.0 4020

bandit20@bandit:~$ ./suconnect  4020
Connection received on localhost 44186
Read: VxCazJaVykI6W36BkBU0mJTCM8rR95XT
Password matches, sending next password
NvEJF7oVjkddltPSrdKEFOllh9V1IBcq
[1]+  Done                    nc -lvp 4020 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT
bandit20@bandit:~$
**Notas adicionales** 

**Referencias** 