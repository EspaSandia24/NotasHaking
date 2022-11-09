# Forensic
## Objetivo
Through tools look for the flag in this [binary](https://drive.google.com/file/d/1YFNZwSLOduHnaJnvtUE5k9FkmQY6J7Nl/view?usp=sharing)
## Pistas
## Solucion

┌─[oscar@oscar-parrot]─[~/Metaredperu/Forensic/GetYourFlag]
└──╼ $file b1n@ri0 
b1n@ri0: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=506b7be935d8940c672ab0d40d2e03ebd746155b, with debug_info, not stripped
┌─[oscar@oscar-parrot]─[~/Metaredperu/Forensic/GetYourFlag]
└──╼ $hexedit 

[1]+  Detenido                hexedit
┌─[✗]─[oscar@oscar-parrot]─[~/Metaredperu/Forensic/GetYourFlag]
└──╼ $hexedit b1n@ri0 


000007D0   01 00 02 00  00 00 00 00  48 65 6C 6C  6F 20 75 73  65 72 21 20  50 61 73 73  20 6D 65 20  61 20 2D 68  20 74 6F 20  6C 65 61 72  ........Hello user! Pass me a -h to lear
000007F8   6E 20 77 68  61 74 20 49  20 63 61 6E  20 64 6F 21  00 2D 68 00  00 00 00 00  4F 68 2C 20  68 65 6C 70  3F 20 49 20  61 63 74 75  n what I can do!.-h.....Oh, help? I actu
00000820   61 6C 6C 79  20 64 6F 6E  27 74 20 64  6F 20 6D 75  63 68 2C 20  62 75 74 20  49 20 64 6F  20 68 61 76  65 20 74 68  69 73 20 66  ally don't do much, but I do have this f
00000848   6C 61 67 20  68 65 72 65  3A 20 66 6C  61 67 7B 54  33 40 6D 5F  48 33 72 45  5F 31 73 5F  79 55 30 72  5F 46 6C 40  47 5F 58 44  lag here: 

flag{T3@m_H3rE_1s_yU0r_Fl@G_XD}

00000870   7D 22 40 40  40 40 40 00  49 20 64 6F  6E 27 74 20  6B 6E 6F 77  20 77 68 61  74 20 27 25  73 27 20 6D  65 61 6E 73  21 20 49 20  }"@@@@@.I don't know what '%s' means! I
00000898   64 6F 20 6B  6E 6F 77 20  77 68 61 74  20 2D 68 20  6D 65 61 6E  73 20 74 68  6F 75 67 68  21 0A 00 00  01 1B 03 3B  3C 00 00 00  do know what -h means though!......;<...



flag{T3@m_H3rE_1s_yU0r_Fl@G_XD}

## Notas Adicionales
## Referencias
