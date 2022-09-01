**Bandit **

**Objetivo**

La contraseña para el siguiente nivel se almacena en **/etc/bandit_pass/bandit14 y solo puede leerla el usuario bandit14** . Para este nivel, no obtiene la siguiente contraseña, pero obtiene una clave SSH privada que puede usarse para iniciar sesión en el siguiente nivel. **Nota:** **localhost** es un nombre de host que se refiere a la máquina en la que está trabajando

**Datos de acceso**
server: **bandit.labs.overthewire.org** 
usuario: **bandit13**
contraseña: 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
**Solucion**
ls -la
file sshkey.private
cat sshkey.private
ssh -i sshkey.private bandit14@localhots
cat /etc/bandit_pass/bandit14

**Notas adicionales** 

**Referencias** 
https://help.ubuntu.com/community/SSH/OpenSSH/Keys