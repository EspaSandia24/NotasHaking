**Bandit **

**Objetivo**

La contraseña para el siguiente nivel se almacena en el archivo **data.txt** , que contiene datos codificados en base64

**Datos de acceso**
server: **bandit.labs.overthewire.org** 
usuario: **bandit10**
contraseña: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
**Solucion**
```bash
bandit10@bandit:~$ ls
data.txt
bandit10@bandit:~$ cat data.txt
VGhlIHBhc3N3b3JkIGlzIElGdWt3S0dzRlc4TU9xM0lSRnFyeEUxaHhUTkViVVBSCg==
bandit10@bandit:~$ cat data.txt |base64 -d
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
bandit10@bandit:~$
```

**Notas adicionales** 

**Referencias** 
https://en.wikipedia.org/wiki/Base64