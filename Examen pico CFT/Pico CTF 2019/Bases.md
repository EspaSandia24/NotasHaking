**Descripcion**

What does this `bDNhcm5fdGgzX3IwcDM1` mean? I think it has something to do with bases.

**Solucion**

usamos el  comando echo para mostrar lo que queremos convertir y agregamos otro comando que hace que nuestro string se canvierta en base 64
```bash
┌──(espasandia24㉿kali)-[~]
└─$ echo bDNhcm5fdGgzX3IwcDM1 | base64 -d 
l3arn_th3_r0p35                                                                             
┌──(espasandia24㉿kali)-[~]
└─$ 

```
picoCTF{l3arn_th3_r0p35}

**Notas Adicionales**