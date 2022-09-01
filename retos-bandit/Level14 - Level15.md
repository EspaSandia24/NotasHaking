**Bandit **

**Objetivo**

La contraseña para el siguiente nivel se puede recuperar enviando la contraseña del nivel actual al **puerto 30000 en localhost** .

**Datos de acceso**
server: **bandit.labs.overthewire.org** 
usuario: **bandit14**
contraseña: 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

**Solucion**
bandit14@bandit:~$ bandit14@bandit:~$ nc localhost 30000 -v                                                    localhost [127.0.0.1] 30000 (?) open                                                                           4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e                                                                               Correct!                                                                                                       BfMYroe26WYalil77FoDi9qh59eK5xNr                                                                                                                                                                                              bandit14@bandit:~$

**Notas adicionales** 

**Referencias** 
https://www.youtube.com/watch?v=7_LPdttKXPc
http://computer.howstuffworks.com/web-server5.htm
https://en.wikipedia.org/wiki/IP_address
https://en.wikipedia.org/wiki/Localhost
http://computer.howstuffworks.com/web-server8.htm
https://en.wikipedia.org/wiki/Port_(computer_networking)
