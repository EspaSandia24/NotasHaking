**Descripcion**

Download this disk image, find the key and log into the remote machine. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

**Solucion**
```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ wget https://artifacts.picoctf.net/c/374/disk.img.gz
--2022-11-10 08:17:05--  https://artifacts.picoctf.net/c/374/disk.img.gz
Resolviendo artifacts.picoctf.net (artifacts.picoctf.net)... 13.249.85.36, 13.249.85.47, 13.249.85.77, ...
Conectando con artifacts.picoctf.net (artifacts.picoctf.net)[13.249.85.36]:443... conectado.
Petición HTTP enviada, esperando respuesta... 200 OK
Longitud: 48132743 (46M) [application/octet-stream]
Grabando a: «disk.img.gz»

disk.img.gz         100%[===================>]  45.90M   897KB/s    en 63s     

2022-11-10 08:18:21 (746 KB/s) - «disk.img.gz» guardado [48132743/48132743]

                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ ls
 disk.img.gz  'Operation Oni.md'
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ ls -la   
total 47013
drwxrwx--- 1 root vboxsf        0 nov 10 08:17  .
drwxrwx--- 1 root vboxsf     4096 nov  9 13:30  ..
-rwxrwx--- 1 root vboxsf 48132743 mar 15  2022  disk.img.gz
-rwxrwx--- 1 root vboxsf      290 nov 10 08:15 'Operation Oni.md'
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ ls -lab
total 47013
drwxrwx--- 1 root vboxsf        0 nov 10 08:17 .
drwxrwx--- 1 root vboxsf     4096 nov  9 13:30 ..
-rwxrwx--- 1 root vboxsf 48132743 mar 15  2022 disk.img.gz
-rwxrwx--- 1 root vboxsf      290 nov 10 08:15 Operation\ Oni.md
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ gzip disk.img.gz   
gzip: disk.img.gz already has .gz suffix -- unchanged
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ ls     
 disk.img.gz  'Operation Oni.md'
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ gzip -d disk.img.gz 
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ ls -lab
total 235525
drwxrwx--- 1 root vboxsf         0 nov 10 08:21 .
drwxrwx--- 1 root vboxsf      4096 nov  9 13:30 ..
-rwxrwx--- 1 root vboxsf 241172480 mar 15  2022 disk.img
-rwxrwx--- 1 root vboxsf       290 nov 10 08:15 Operation\ Oni.md
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ mmls disk.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000471039   0000264192   Linux (0x83)
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ man fls      
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ fls -o 471039 disk.img 
Cannot determine file system type
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ fls -o 471040 disk.img
Sector offset supplied is larger than disk image (maximum: 471040)
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ fls -o 264192 disk.img
Cannot determine file system type
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ man fls
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ fls -o 206848 disk.img
d/d 458:        home
d/d 11: lost+found
d/d 12: boot
d/d 13: etc
d/d 79: proc
d/d 80: dev
d/d 81: tmp
d/d 82: lib
d/d 85: var
d/d 94: usr
d/d 104:        bin
d/d 118:        sbin
d/d 464:        media
d/d 468:        mnt
d/d 469:        opt
d/d 470:        root
d/d 471:        run
d/d 473:        srv
d/d 474:        sys
V/V 33049:      $OrphanFiles
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ fls -o 206848 disk.img 470
r/r 2344:       .ash_history
d/d 3916:       .ssh
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ fls -o 206848 disk.img 470 3916
Error stat(ing) image file (raw_open: image "470" - No existe el fichero o el directorio)
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ fls -o 206848 disk.img 3916    
r/r 2345:       id_ed25519
r/r 2346:       id_ed25519.pub
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ icat -o 206848 disk.img 2345
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLAAAAJgxpYKDMaWC
gwAAAAtzc2gtZWQyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLA
AAAECItu0F8DIjWxTp+KeMDvX1lQwYtUvP2SfSVOfMOChxYGCtd7hso2E7OQItY6aTjMMy
KZb1FVmeBfnVjyHcGYosAAAADnJvb3RAbG9jYWxob3N0AQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ icat -o 206848 disk.img 2345 > key
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ 
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ ls     
 disk.img   key  'Operation Oni.md'
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ cat key             
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLAAAAJgxpYKDMaWC
gwAAAAtzc2gtZWQyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLA
AAAECItu0F8DIjWxTp+KeMDvX1lQwYtUvP2SfSVOfMOChxYGCtd7hso2E7OQItY6aTjMMy
KZb1FVmeBfnVjyHcGYosAAAADnJvb3RAbG9jYWxob3N0AQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ chmod 400 key 
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ ls -la 
total 235525
drwxrwx--- 1 root vboxsf         0 nov 10 08:29  .
drwxrwx--- 1 root vboxsf      4096 nov  9 13:30  ..
-rwxrwx--- 1 root vboxsf 241172480 mar 15  2022  disk.img
-rwxrwx--- 1 root vboxsf       411 nov 10 08:29  key
-rwxrwx--- 1 root vboxsf       290 nov 10 08:15 'Operation Oni.md'
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ ssh -i key_file -p 55607 ctf-player@saturn.picoctf.net
Warning: Identity file key_file not accessible: No such file or directory.
The authenticity of host '[saturn.picoctf.net]:55607 ([18.217.86.78]:55607)' can't be established.
ED25519 key fingerprint is SHA256:5gIm/EJ9bYnoH4qed83W5HXLfN1DO55849f6Lze0lx8.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? y
Please type 'yes', 'no' or the fingerprint: yes
Warning: Permanently added '[saturn.picoctf.net]:55607' (ED25519) to the list of known hosts.
ctf-player@saturn.picoctf.net's password: 
Permission denied, please try again.
ctf-player@saturn.picoctf.net's password: 

Permission denied, please try again.
ctf-player@saturn.picoctf.net's password: 
ctf-player@saturn.picoctf.net: Permission denied (publickey,password).
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ ls    
 disk.img   key_file  'Operation Oni.md'
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Forensic/Operation Oni]
└─$ ssh -i key_file -p 55607 ctf-player@saturn.picoctf.net
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.13.0-1025-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@challenge:~$ ls
flag.txt
ctf-player@challenge:~$ cat flag.txt 
picoCTF{k3y_5l3u7h_af277f77}ctf-player@challenge:~$ 

```
picoCTF{k3y_5l3u7h_af277f77}
**Notas Adicionales**