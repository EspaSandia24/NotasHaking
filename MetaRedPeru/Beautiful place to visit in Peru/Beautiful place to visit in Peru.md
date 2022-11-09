# Forensic
## Objetivo
Do you know the beautiful places that Peru has? I'll give you some clues so you can discover them. A file has been transferred with the list of some interesting places in Peru that you should know. Find out which place we recommend you visit.

Locate a clue that will lead you to discover the chosen place

https://metaredperu.ctfd.io/files/6e5fa071a02794d3988f078646cbe0ce/lugares.pcapng?token=eyJ1c2VyX2lkIjoyNDMwLCJ0ZWFtX2lkIjo1MDYsImZpbGVfaWQiOjZ9.Y2nuUQ.9nmgvGKR_aNyNBCtKZvIXI8Kwtc
## Pistas
## Solucion

1)
Usando WIreShark se sigue el flujo de los datos TCP hasta la secuencia 17
	captura
Se modifica para que muestre los datos como RAW
	captura2
Se guarda como...  y se le da un formato .zip

┌─[oscar@oscar-parrot]─[~/Metaredperu/Forensic/BeautifulPlaceToVisitInPeru]
└──╼ $cd elchido/
┌─[oscar@oscar-parrot]─[~/Metaredperu/Forensic/BeautifulPlaceToVisitInPeru/elchido]
└──╼ $ls
Flag.zip
┌─[oscar@oscar-parrot]─[~/Metaredperu/Forensic/BeautifulPlaceToVisitInPeru/elchido]
└──╼ $unzip Flag.zip 
Archive:  Flag.zip
[Flag.zip] Flag.jpg password: 
  inflating: Flag.jpg                
  inflating: Lista de lugares por visitar.txt  
┌─[oscar@oscar-parrot]─[~/Metaredperu/Forensic/BeautifulPlaceToVisitInPeru/elchido]
└──╼ $ls
 Flag.jpg   Flag.zip  'Lista de lugares por visitar.txt'
┌─[oscar@oscar-parrot]─[~/Metaredperu/Forensic/BeautifulPlaceToVisitInPeru/elchido]
└──╼ $cat Lista\ de\ lugares\ por\ visitar.txt 
Machu Pichu --> Cuzco
Baños del Inca --> Cajamarca
Kuélap --> Amazonas
Valle del Colca --> Arequipa
Callejón de Huaylas --> Anchash
Señor de Sipán --> Lambayeque
Chan Chan -->  La Libertad
Meseta de Marcahuasi -->Lima-Provincias
Gran Pajatén --> San Martín- La libertad
Bosque de piedras de Huayllay --> Pasco
Lago Titicaca --> Puno
Líneas de Nazca --> Ica
Choquequirao --> Cuzco┌─[oscar@oscar-parrot]─[~/Metaredperu/Forensic/BeautifulPlaceToVisitInPeru/elchido]
└──╼ $strings Lista\ de\ lugares\ por\ visitar.txt 
Machu Pichu --> Cuzco
os del Inca --> Cajamarca
lap --> Amazonas
Valle del Colca --> Arequipa
Callej
n de Huaylas --> Anchash
or de Sip
n --> Lambayeque
Chan Chan -->  La Libertad
Meseta de Marcahuasi -->Lima-Provincias
Gran Pajat
n --> San Mart
n- La libertad
Bosque de piedras de Huayllay --> Pasco
Lago Titicaca --> Puno
neas de Nazca --> Ica
Choquequirao --> Cuzco
┌─[oscar@oscar-parrot]─[~/Metaredperu/Forensic/BeautifulPlaceToVisitInPeru/elchido]
└──╼ $open Flag.jpg 
┌─[oscar@oscar-parrot]─[~/Metaredperu/Forensic/BeautifulPlaceToVisitInPeru/elchido]
└──╼ $


## Notas Adicionales
## Referencias