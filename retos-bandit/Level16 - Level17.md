**Bandit **

**Objetivo**

Las credenciales para el siguiente nivel se pueden recuperar enviando la contraseña del nivel actual a **un puerto en localhost en el rango 31000 a 32000** . Primero averigüe cuáles de estos puertos tienen un servidor escuchando en ellos. Luego, averigüe cuáles de ellos hablan SSL y cuáles no. Solo hay 1 servidor que proporcionará las siguientes credenciales, los demás simplemente le enviarán lo que le envíe.

**Datos de acceso**
server: **bandit.labs.overthewire.org** 
usuario: **bandit16**
contraseña: 

**Solucion**
nmap  localhost
nmap  localhost -p 31000-32000
oppenssl s_client -connect localhost:31046
oppenssl s_client -connect localhost:31790

#en_la_maquina
nano lallave
cat lallave
ls -la
chmod 600 lallave
ls -la

ssh -i lallave bandit16@localhots
cat /etc/bandit_pass/bandit17

**Notas adicionales** 

**Referencias** 
https://en.wikipedia.org/wiki/Port_scanner