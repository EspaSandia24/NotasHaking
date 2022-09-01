**Bandit **

**Objetivo**

La contraseña para el siguiente nivel se almacena en el archivo **data.txt** , que es un volcado hexadecimal de un archivo que ha sido comprimido repetidamente. Para este nivel, puede ser útil crear un directorio bajo /tmp en el que pueda trabajar usando mkdir. Por ejemplo: mkdir /tmp/myname123. Luego copie el archivo de datos usando cp, y cámbiele el nombre usando mv (¡lea las páginas de manual!)

**Datos de acceso**
server: **bandit.labs.overthewire.org** 
usuario: **bandit12**
contraseña: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

**Solucion**
bandit12@bandit:~$ cat data.txt | xxd -r
J쌑Oϊ{RBpQixYZ!dj(搿ݳ/A#dbX?z2<A n}4hFF4LM@zFMChFC@4@fhihPhMh
5(3AwOR6XS{
9?LPyB=zm?LNt*7{qP̜%"w9qm4 N36KH䋑[}!d3A4$M~\JCkUƦ\\FSN&=[q      \)$:Ht&/(]BB9<s h=bandit12@bandit:~$ cat data.txt | xxd -r | file -
/dev/stdin: gzip compressed data, was "data2.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
bandit12@bandit:~$ cat data.txt | xxd -r |zcat| file -
/dev/stdin: bzip2 compressed data, block size = 900k
bandit12@bandit:~$ cat data.txt | xxd -r |zcat|bzcat|file -
/dev/stdin: gzip compressed data, was "data4.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
bandit12@bandit:~$ cat data.txt | xxd -r |zcat|bzcat|zcat|file -
/dev/stdin: POSIX tar archive (GNU)
bandit12@bandit:~$ cat data.txt | xxd -r |zcat|bzcat|zcat|tar xO|file -
/dev/stdin: POSIX tar archive (GNU)
bandit12@bandit:~$ cat data.txt | xxd -r |zcat|bzcat|zcat|tar xO|tar xO|file -
/dev/stdin: bzip2 compressed data, block size = 900k
bandit12@bandit:~$ cat data.txt | xxd -r |zcat|bzcat|zcat|tar xO|tar xO|bzcat|file
-
/dev/stdin: POSIX tar archive (GNU)
bandit12@bandit:~$ cat data.txt | xxd -r |zcat|bzcat|zcat|tar xO|tar xO|bzcat|tar xO|file -
/dev/stdin: gzip compressed data, was "data9.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
bandit12@bandit:~$ cat data.txt | xxd -r |zcat|bzcat|zcat|tar xO|tar xO|bzcat|tar xO|zcat|file -
/dev/stdin: ASCII text


**Notas adicionales** 
el -d  y xf sirvepara descomprime  en el disco
para descomprimir en pantalla es lo siguiente 
zcat para descomprimir .gz
bzcat para descomprimir .bzz
tar xo para descoprimir .tar
xxd sirve para convertir en Hexadecimal

**Referencias** 
https://en.wikipedia.org/wiki/Hex_dump