**Descripcion**

Find the flag in this [picture](https://jupiter.challenges.picoctf.org/static/00efdf2961da1e21470ffc0d496c3cc2/pico_img.png).

**Solucion**
```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/So Meta]
└─$ ls 
 pico_img.png  'So Meta.md'
                                                                                 
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/So Meta]
└─$ exiftool --help                     
Syntax:  exiftool [OPTIONS] FILE

Consult the exiftool documentation for a full list of options.
                                                                                 
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/So Meta]
└─$ exiftool pico_img.png 
ExifTool Version Number         : 12.44
File Name                       : pico_img.png
Directory                       : .
File Size                       : 109 kB
File Modification Date/Time     : 2022:10:16 14:19:10-05:00
File Access Date/Time           : 2022:10:16 14:22:38-05:00
File Inode Change Date/Time     : 2022:10:16 14:19:10-05:00
File Permissions                : -rwxrwx---
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 600
Image Height                    : 600
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Software                        : Adobe ImageReady
XMP Toolkit                     : Adobe XMP Core 5.3-c011 66.145661, 2012/02/06-14:56:27
Creator Tool                    : Adobe Photoshop CS6 (Windows)
Instance ID                     : xmp.iid:A5566E73B2B811E8BC7F9A4303DF1F9B
Document ID                     : xmp.did:A5566E74B2B811E8BC7F9A4303DF1F9B
Derived From Instance ID        : xmp.iid:A5566E71B2B811E8BC7F9A4303DF1F9B
Derived From Document ID        : xmp.did:A5566E72B2B811E8BC7F9A4303DF1F9B
Warning                         : [minor] Text/EXIF chunk(s) found after PNG IDAT (may be ignored by some readers)
Artist                          : picoCTF{s0_m3ta_fec06741}
Image Size                      : 600x600
Megapixels                      : 0.360
                                                                                 
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/So Meta]
└─$ 

```
picoCTF{s0_m3ta_fec06741}