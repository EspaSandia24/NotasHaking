**Bandit **

**Objetivo**

**Datos de acceso**
server: **bandit.labs.overthewire.org** 
usuario: **bandit11**
contraseña: 

**Solucion**
ls
ls -la
file data.txt
cat data.txt
cat data.txt | xxd -r
cat data.txt | xxd -r | file -
cat data.txt | xxd -r | zcat | file -
cat data.txt | xxd -r | zcat | bzcat| file -
cat data.txt | xxd -r | zcat | bzcat| zcat | file -
cat data.txt | xxd -r | zcat | bzcat| zcat | tar xO | file -
cat data.txt | xxd -r | zcat | bzcat| zcat | tar xO | tar xO | file -
cat data.txt | xxd -r | zcat | bzcat | zcat | tar xO | tar xO | bzcar|file -
cat data.txt | xxd -r | zcat | bzcat | zcat | tar xO| tar xO | bzcar|tar ox|file -
cat data.txt | xxd -r | zcat | bzcat | zcat | tar xO| tar xO | bzcar | tar xO | zcat | file -


**Notas adicionales** 
el -d  y xf sirvepara descomprime  en el disco
para descomprimir en pantalla es lo siguiente 
zcat para descomprimir .gz
bzcat para descomprimir .bzz
tar xo para descoprimir .tar
xxd sirve para convertir en Hexadecimal

**Referencias** 