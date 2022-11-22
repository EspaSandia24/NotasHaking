# CTF META Forensic
# Equipo Dinamita 2.0
## Objetivo
A criminal escaped from jail. The only clue that we have is this file. Help us to find out where he is.

flag{CITY,COUNTRY}
## Pistas
## Solucion
┌─[oscar@oscar-parrot]─[~/CTFMetaEcu/Forensic/Drain]
└──╼ $exiftool you 
ExifTool Version Number         : 12.16
File Name                       : you
Directory                       : .
File Size                       : 3.2 MiB
File Modification Date/Time     : 2022:11:21 22:31:06-06:00
File Access Date/Time           : 2022:11:21 22:31:05-06:00
File Inode Change Date/Time     : 2022:11:21 22:31:24-06:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
Exif Byte Order                 : Big-endian (Motorola, MM)
Make                            : Xiaomi
Camera Model Name               : M2102J20SG
Orientation                     : Horizontal (normal)
X Resolution                    : 72
Y Resolution                    : 72
Resolution Unit                 : inches
Modify Date                     : 2022:10:09 16:37:42
Y Cb Cr Positioning             : Centered
Exposure Time                   : 1/294
F Number                        : 1.8
Exposure Program                : Program AE
ISO                             : 50
Exif Version                    : 0220
Date/Time Original              : 2022:10:09 16:37:42
Create Date                     : 2022:10:09 16:37:42
Components Configuration        : Y, Cb, Cr, -
Shutter Speed Value             : 1/293
Aperture Value                  : 1.8
Brightness Value                : 4.88
Exposure Compensation           : 0
Max Aperture Value              : 1.8
Metering Mode                   : Center-weighted average
Light Source                    : D65
Flash                           : Off, Did not fire
Focal Length                    : 4.7 mm
Sub Sec Time                    : 750
Sub Sec Time Original           : 750
Sub Sec Time Digitized          : 750
Flashpix Version                : 0100
Color Space                     : sRGB
Exif Image Width                : 4000
Exif Image Height               : 1800
Interoperability Index          : R98 - DCF basic file (sRGB)
Interoperability Version        : 0100
Sensing Method                  : Not defined
Scene Type                      : Directly photographed
Exposure Mode                   : Auto
White Balance                   : Auto
Focal Length In 35mm Format     : 25 mm
Scene Capture Type              : Standard
GPS Altitude Ref                : Above Sea Level
GPS Time Stamp                  : 21:37:36
GPS Processing Method           : CELLID
GPS Date Stamp                  : 2022:10:09
XMP Toolkit                     : Image::ExifTool 12.47
Owner                           : ...-- / ..... ---.. / ...-- ..--- .-.-.- ....- / ... / --... ----. / .---- ----- / .---- ..... .-.-.- ...-- / .--
Image Width                     : 4000
Image Height                    : 1800
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Aperture                        : 1.8
Image Size                      : 4000x1800
Megapixels                      : 7.2
Scale Factor To 35 mm Equivalent: 5.3
Shutter Speed                   : 1/294
Create Date                     : 2022:10:09 16:37:42.750
Date/Time Original              : 2022:10:09 16:37:42.750
Modify Date                     : 2022:10:09 16:37:42.750
GPS Altitude                    : 2061.6 m Above Sea Level
GPS Date/Time                   : 2022:10:09 21:37:36Z
Circle Of Confusion             : 0.006 mm
Field Of View                   : 71.5 deg
Focal Length                    : 4.7 mm (35 mm equivalent: 25.0 mm)
Hyperfocal Distance             : 2.19 m
Light Value                     : 10.9



Al decodificar codigo morse que aparece, se puede obtener lo siguiente

3/58/32.4/S/79/10/15.3/w

Si lo traducimos a cordenadas, podemos encontrar que estas apuntan a la ciudad mas cercana en coincidencia 

https://www.geodatos.net/coordenadas/ecuador/loja

Flag = flag{LOJA,ECUADOR}

## Notas adicionales
## Referencias