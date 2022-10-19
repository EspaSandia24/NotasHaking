**Descripcion**

Para la clase de arte de María, la maestra pidió una OBRA MAESTRA que combinara la historia y los sentimientos, por lo que María decidió crear una pintura que describiera un evento histórico cercano a su corazón y sus raíces. Decidió pintar una parte de Yucatán con la que todos pudieran identificarse, así que pintó la pirámide de kukulkan. María dice que escondió un pequeño mensaje en la pintura, pero supongo que la maestra nunca lo encontró porque María sacó una F. Ayuda a María a pasar la clase, encuentra el mensaje y envíaselo a la maestra:3

**Solucion**
```bash
──(espasandia24㉿kali)-[~/Escritorio/HakinKali/MetaCTF/Marias]
└─$ ls
KUKULKAN.jpg
                                                                                 
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/MetaCTF/Marias]
└─$ strings KUKULKAN.jpg |grep FLAG     
_I LOVE FLAGS :3 
.MY FAVOURITE WORD IS FLAG 
THIS IS NOT THE FLAG, KEEP LOOKING BRO! 
/ FLAG Un PAso mas  BRO{Vm0weGQxTnRVWGxXYTFwUFZsZG9WRmxVU2xOalJsSlZVMnhPVlUxV2NEQlVWbEpUWVdzeFYxTnNhRmRpVkZaUVZrUktTMUl5VGtsaVJtUk9ZbTFvZVZadE1YcGxSbGw0Vkc1V2FsSnNXazlXYlRWRFYxWmFkR1JIUmxSTlZYQjVWR3hhYjFSc1duTmpSVGxhWWxoU1RGWnNXbUZXVmtaMFVteHdWMkpJUWpaV1ZFa3hWREZhV0ZOclpHcFNWR3hZV1ZSS1VrMUdWWGRYYlVacVZtdHdlbGRyV210VWJGcDFVV3R3VjJGcmJ6QlZla1pYVmpGa2NsWnNTbGRTTTAwMQ==}   x
                                                                                 
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/MetaCTF/Marias]
└─$ 

```
la cadena dada la decodificamos en base64 8 veces hasta optener la bandera
![[Pasted image 20221018224619.png]]
![[Pasted image 20221018224731.png]]
![[Pasted image 20221018224910.png]]
![[Pasted image 20221018225003.png]]
![[Pasted image 20221018225109.png]]
![[Pasted image 20221018225138.png]]
![[Pasted image 20221018225336.png]]
![[Pasted image 20221018225609.png]]
![[Pasted image 20221018225647.png]]
flagMX{R3TURN_TH3_J4GUARS_EYES}