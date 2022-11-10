**Descripcion**

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/e5825f58ef798fdd1af3f6013592a971/cat.jpg)

**Solucion**

```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/information]
└─$ wget https://mercury.picoctf.net/static/e5825f58ef798fdd1af3f6013592a971/cat.jpg
--2022-11-09 13:44:21--  https://mercury.picoctf.net/static/e5825f58ef798fdd1af3f6013592a971/cat.jpg
Resolviendo mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Conectando con mercury.picoctf.net (mercury.picoctf.net)[18.189.209.142]:443... conectado.
Petición HTTP enviada, esperando respuesta... 200 OK
Longitud: 878136 (858K) [application/octet-stream]
Grabando a: «cat.jpg»

cat.jpg             100%[===================>] 857.55K  1.64MB/s    en 0.5s    

2022-11-09 13:44:23 (1.64 MB/s) - «cat.jpg» guardado [878136/878136]

                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/information]
└─$ ls 
cat.jpg  Information.md
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/information]
└─$ file cat.jpg 
cat.jpg: JPEG image data, JFIF standard 1.02, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2560x1598, components 3
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/information]
└─$ exiftool cat.jpg       
ExifTool Version Number         : 12.44
File Name                       : cat.jpg
Directory                       : .
File Size                       : 878 kB
File Modification Date/Time     : 2021:03:15 12:24:46-06:00
File Access Date/Time           : 2022:11:09 13:44:27-06:00
File Inode Change Date/Time     : 2022:11:09 13:44:25-06:00
File Permissions                : -rwxrwx---
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/information]
└─$ echo cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 | base64 
Y0dsamIwTlVSbnQwYUdWZmJUTjBZV1JoZEdGZk1YTmZiVzlrYVdacFpXUjkK
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/information]
└─$ echo cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 | base64 -d 
picoCTF{the_m3tadata_1s_modified}                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2021/Forensic/information]
└─$ 


```
picoCTF{the_m3tadata_1s_modified}

**Notas Adicionales**