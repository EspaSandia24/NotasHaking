# CTF META
## Objetivo

Pablito took a visit to Hubikú, a huge cenote near to Chichen Itzá in Yucatán. While Pablito was swimming in the darkest part of the cenote, a little light coming out from a Wall of rocks caught his atention.

As he explored the Wall, he found a series of paintings, rare ones, so Pablito instead of calling the authorities, he decided to take a picture and Google it to find out what does it mean.

Help Pablito to make the discover of the century.

<�div class="row challenge-files text-center pb-3"> <�div class="col-md-4 col-sm-4 col-xs-12 file-button-wrapper d-block"> <�a class="btn btn-info btn-file mb-1 d-inline-block px-2 w-100 text-truncate" href="https://ctfd2022.anuies.mx/files/2211914d1a093902ffe389f9e9e133d9/Pablito_Visits_Hubiku.png?token=eyJ1c2VyX2lkIjoxODgzLCJ0ZWFtX2lkIjo1MDYsImZpbGVfaWQiOjl9.Y09tpQ.W_7a2hGeJjnakLTG8ncVp1BpvD8"> <�i class="fas fa-download"><�/i> <�small> Pablito_Visits_Hubiku.png <�/small> <�/a> <�/div> <�/div>

## Pistas
## Solucion

┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/PablitoVisitsHubiku100]
└──╼ $ls
'Pablito_Visits_Hubiku.png?token=eyJ1c2VyX2lkIjoxODgzLCJ0ZWFtX2lkIjo1MDYsImZpbGVfaWQiOjl9.Y09tpQ.W_7a2hGeJjnakLTG8ncVp1BpvD8'
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/PablitoVisitsHubiku100]
└──╼ $strings Pablito_Visits_Hubiku.png\?token\=eyJ1c2VyX2lkIjoxODgzLCJ0ZWFtX2lkIjo1MDYsImZpbGVfaWQiOjl9.Y09tpQ.W_7a2hGeJjnakLTG8ncVp1BpvD8 | grep FLAG
┌─[✗]─[oscar@oscar-parrot]─[~/CTFMETA/crypto/PablitoVisitsHubiku100]
└──╼ $mv Pablito_Visits_Hubiku.png\?token\=eyJ1c2VyX2lkIjoxODgzLCJ0ZWFtX2lkIjo1MDYsImZpbGVfaWQiOjl9.Y09tpQ.W_7a2hGeJjnakLTG8ncVp1BpvD8 Pablito_Visits_Hubiku.png
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/PablitoVisitsHubiku100]
└──╼ $open Pablito_Visits_Hubiku.png 
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/PablitoVisitsHubiku100]
└──╼ $nano flag.txt

*Se traduce los simbolos mayas que estan en la imagen con ayuda de la Imagen1 y Imagen2*

flagMX{M4YAN5_R0KK5}




## Notas adicionales
## Referencias