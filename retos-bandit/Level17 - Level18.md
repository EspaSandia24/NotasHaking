**Bandit **

**Objetivo**

Hay 2 archivos en el directorio de inicio: **passwords.old y passwords.new** . La contraseña para el siguiente nivel está en **passwords.new** y es la única línea que se ha cambiado entre **passwords.old y passwords.new**

**NOTA: si ha resuelto este nivel y ve '¡Adiós!' al intentar iniciar sesión en bandit18, esto está relacionado con el siguiente nivel, bandit19**

**Datos de acceso**
server: **bandit.labs.overthewire.org** 
usuario: **bandit17**
contraseña: VwOSWtCA7lRKkTfbr2IDh6awj9RNZM5e

**Solucion**
bandit17@bandit:~$ ls
passwords.new  passwords.old
bandit17@bandit:~$ head passwords.old
AaRtLcWpaZf2x05CinBQoTjVP6fML7EA
VyuddgCO0UtJKMwC7H4vxAaIMGjPiqky
gLdNHXq36zoT1HFfPYk4kw5h1Ixyqcvo
q6qV3SwGPS7L0cw3aJA21lzhNMrAQcGC
s1vg97taODeKBsWz5yVTIumCUQGggQEC
ufsx6BLBrGbOAm5LftWxyvYvEpGPeHhv
uLgMlo2nIcUwbm4oyKuwwo8KoT9eP6Oe
dixsvhg78iuQJ5t2c2UbRLvwbJrbZF1n
Wx2PczEyROiv1UYMIVpmXaljcRWMB52b
wQs6u5FBMsS4Y1NGzQS7W2sv6NnmbJ2i
bandit17@bandit:~$ wc passwords.old
 100  100 3300 passwords.old
bandit17@bandit:~$ wc passwords.new
 100  100 3300 passwords.new
bandit17@bandit:~$ diff passwords.old passwords.new
42c42
< 09wUIyMU4YhOzl1Lzxoz0voIBzZ2TUAf
---
> hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg


**Notas adicionales** 
dif conpara archivos
**Referencias** 