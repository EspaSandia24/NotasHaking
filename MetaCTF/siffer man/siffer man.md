**Descripcion**
Mi organización ha aprendido sobre seguridad cibernética de la manera más difícil en los últimos años.

**Solucion**
```bash
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/MetaCTF/siffer man]
└─$ ls
challenge.pcapng
                                                                                 
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/MetaCTF/siffer man]
└─$ file challenge.pcapng  
challenge.pcapng: pcapng capture file - version 1.0
                                                                                 
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/MetaCTF/siffer man]
└─$ wireshark challenge.pcapng
```
revisando los paquetes encontramos lo siguiente

![[Pasted image 20221018230932.png]]

xdsyEP{E2f_9f_Lz1_E9vvd1_2ll2uc}

![[Pasted image 20221019124535.png]]
flagMX{M2n_9n_Th1_M9ddl1_2tt2ck}

modificamos la bandera cambiando los 2 por 4 los 9 por 1 y los 1 por 3

flagMX{M4n_1n_Th3_M1ddl3_4tt4ck}