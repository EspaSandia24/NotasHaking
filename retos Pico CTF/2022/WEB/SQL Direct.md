**Descripcion**

Connect to this PostgreSQL server and find the flag!

**Solucion**

```bash
┌──(espasandia24㉿kali)-[~]
└─$ psql -h saturn.picoctf.net -p 49223 -U postgres pico
Contraseña para usuario postgres: 
psql (14.4 (Debian 14.4-1+b1), servidor 14.2 (Debian 14.2-1.pgdg110+1))
Digite «help» para obtener ayuda.

pico=# \d
        Listado de relaciones
 Esquema | Nombre | Tipo  |  Dueño   
---------+--------+-------+----------
 public  | flags  | tabla | postgres
(1 fila)

pico=# selec * from flags;
ERROR:  syntax error at or near "selec"
LÍNEA 1: selec * from flags;
         ^
pico=# select * from flags;
 id | firstname | lastname  |                address                 
----+-----------+-----------+----------------------------------------
  1 | Luke      | Skywalker | picoCTF{L3arN_S0m3_5qL_t0d4Y_73b0678f}
  2 | Leia      | Organa    | Alderaan
  3 | Han       | Solo      | Corellia
(3 filas)

pico=# exit
                                                                                
┌──(espasandia24㉿kali)-[~]
└─$ 

```
picoCTF{L3arN_S0m3_5qL_t0d4Y_73b0678f}
**Notas Adicionales**