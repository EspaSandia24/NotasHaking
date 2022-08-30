**Bandit **

**Objetivo**


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