**Bandit **

**Objetivo**

La contraseña para el siguiente nivel se puede recuperar enviando la contraseña del nivel actual al **puerto 30001 en localhost** usando encriptación SSL.

**Nota útil: ¿Obtienes "HEARTBEATING" y "Read R BLOCK"? Use -ign_eof y lea la sección "COMANDOS CONECTADOS" en la página de manual. Junto a 'R' y 'Q', el comando 'B' también funciona en esta versión de ese comando...**

**Datos de acceso**
server: **bandit.labs.overthewire.org** 
usuario: **bandit15**
contraseña: 
**Solucion**
openssl s_client -connect localhost:30001


**Notas adicionales** 

**Referencias** 
https://en.wikipedia.org/wiki/Secure_Socket_Layer
https://www.feistyduck.com/library/openssl-cookbook/online/ch-testing-with-openssl.html
