**Descripcion**



**Solucion**
```bash

┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ ls
tftp.pcapng  Untitled.md
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ ls -la
total 50901
drwxrwx--- 1 root vboxsf        0 oct 11 08:39 .
drwxrwx--- 1 root vboxsf     4096 oct 11 08:36 ..
-rwxrwx--- 1 root vboxsf 52116496 oct 11 08:39 tftp.pcapng
-rwxrwx--- 1 root vboxsf       55 oct 11 08:35 Untitled.md
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ ls -lah
total 50M
drwxrwx--- 1 root vboxsf    0 oct 11 08:39 .
drwxrwx--- 1 root vboxsf 4.0K oct 11 08:36 ..
-rwxrwx--- 1 root vboxsf  50M oct 11 08:39 tftp.pcapng
-rwxrwx--- 1 root vboxsf   55 oct 11 08:35 Untitled.md
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ wireshark tftp.pcapng &
[1] 16771
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ ls     
instructions.txt  picture2.bmp  plan         tftp.pcapng
picture1.bmp      picture3.bmp  program.deb  Untitled.md
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ cat instructions.txt                 
GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ cat instructions.txt | tr [A-Z][N-ZA-M]
tr: falta un operando después de «[A-Z][N-ZA-M]»
Al traducir se deben proporcionar dos cadenas.
Pruebe 'tr --help' para más información.
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ cat instructions.txt | tr [A-Z] [N-ZA-M]
TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ cat plan                                
VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ cat plan | tr [A-Z] [N-ZA-M]
IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ 
[1]  + done       wireshark tftp.pcapng
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ dpkg -I program.deb 
 paquete Debian nuevo, versión 2.0.
 tamaño 138310 bytes: archivo de control= 1250 bytes.
     826 bytes,    18 líneas     control              
    1184 bytes,    17 líneas     md5sums              
 Package: steghide
 Source: steghide (0.5.1-9.1)
 Version: 0.5.1-9.1+b1
 Architecture: amd64
 Maintainer: Ola Lundqvist <opal@debian.org>
 Installed-Size: 426
 Depends: libc6 (>= 2.2.5), libgcc1 (>= 1:4.1.1), libjpeg62-turbo (>= 1:1.3.1), libmcrypt4, libmhash2, libstdc++6 (>= 4.9), zlib1g (>= 1:1.1.4)
 Section: misc
 Priority: optional
 Description: A steganography hiding tool
  Steghide is steganography program which hides bits of a data file
  in some of the least significant bits of another file in such a way
  that the existence of the data file is not visible and cannot be proven.
  .
  Steghide is designed to be portable and configurable and features hiding
  data in bmp, wav and au files, blowfish encryption, MD5 hashing of
  passphrases to blowfish keys, and pseudo-random distribution of hidden bits
  in the container data.
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ ls                 
instructions.txt  picture2.bmp  plan         tftp.pcapng
picture1.bmp      picture3.bmp  program.deb  Untitled.md
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ dpkg -i program.deb
dpkg: error: la operación solicitada precisa privilegios de superusuario
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ sudo dpkg -i program.deb  
[sudo] contraseña para espasandia24: 
Seleccionando el paquete steghide previamente no seleccionado.
(Leyendo la base de datos ... 310988 ficheros o directorios instalados actualmente.)
Preparando para desempaquetar program.deb ...
Desempaquetando steghide (0.5.1-9.1+b1) ...
dpkg: problemas de dependencias impiden la configuración de steghide:
 steghide depende de libmcrypt4; sin embargo:
  El paquete `libmcrypt4' no está instalado.
 steghide depende de libmhash2; sin embargo:
  El paquete `libmhash2' no está instalado.

dpkg: error al procesar el paquete steghide (--install):
 problemas de dependencias - se deja sin configurar
Procesando disparadores para man-db (2.10.2-1) ...

^Cdpkg: error al procesar el paquete man-db (--install):
 se interrumpió el subproceso instalado paquete man-db script post-installation
Procesando disparadores para kali-menu (2022.3.1) ...

^XSe encontraron errores al procesar:
 steghide
 man-db
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ sudo dpkg -i program.deb
(Leyendo la base de datos ... 311006 ficheros o directorios instalados actualmente.)
Preparando para desempaquetar program.deb ...
Desempaquetando steghide (0.5.1-9.1+b1) sobre (0.5.1-9.1+b1) ...
dpkg: problemas de dependencias impiden la configuración de steghide:
 steghide depende de libmcrypt4; sin embargo:
  El paquete `libmcrypt4' no está instalado.
 steghide depende de libmhash2; sin embargo:
  El paquete `libmhash2' no está instalado.

dpkg: error al procesar el paquete steghide (--install):
 problemas de dependencias - se deja sin configurar
Procesando disparadores para kali-menu (2022.3.1) ...
Se encontraron errores al procesar:
 steghide
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ steghide --extract -sf picture1.bmp -p DUEDILIGENCE
steghide: error while loading shared libraries: libmcrypt.so.4: cannot open shared object file: No such file or directory
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ steghide --extract -sf picture2.bmp -p DUEDILIGENCE
steghide: error while loading shared libraries: libmcrypt.so.4: cannot open shared object file: No such file or directory
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ steghide --extract -sf picture3.bmp -p DUEDILIGENCE
steghide: error while loading shared libraries: libmcrypt.so.4: cannot open shared object file: No such file or directory
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ sudo apt install steghide                          
Leyendo lista de paquetes... Hecho
Creando árbol de dependencias... Hecho
Leyendo la información de estado... Hecho
Tal vez quiera ejecutar «apt --fix-broken install» para corregirlo.
Los siguientes paquetes tienen dependencias incumplidas:
 mariadb-server-10.6 : Depende: mariadb-client-10.6 (>= 1:10.6.9-1) pero 1:10.6.8-1 va a ser instalado
                       Depende: mariadb-server-core-10.6 (>= 1:10.6.9-1) pero 1:10.6.8-1 va a ser instalado
 steghide : Depende: libmcrypt4 pero no va a instalarse
            Depende: libmhash2 (>= 0.9.9.9) pero no va a instalarse
E: Dependencias incumplidas. Intente «apt --fix-broken install» sin paquetes (o especifique una solución).
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ steghide --extract -sf picture3.bmp -p DUEDILIGENCE
steghide: error while loading shared libraries: libmcrypt.so.4: cannot open shared object file: No such file or directory
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/Trivial Flag Transfer Protocol]
└─$ 

```

**Notas Adicionales**