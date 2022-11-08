**Descripcion**

Unzip this [archive](https://drive.google.com/file/d/15pFs7BTOuJ4jrHZOAHNXfPWunY0K9fGl/view?usp=sharing) and find the file named 'oliver_twist.txt'

**Solucion**

buscamos en  las carpetas una carpeta  secreta  donde indagamos en las carpetas y encontramos el archivo y lo leemos y da la bandera.

```bash
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/MetaRedPeru/find flag]
└─$ ls
great_author.zip
                                                                                
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/MetaRedPeru/find flag]
└─$ unzip great_author.zip 
Archive:  great_author.zip
   creating: great_author/
  inflating: great_author/14789.txt.utf-8  
  inflating: great_author/13771.txt.utf-8  
   creating: great_author/adequate_books/
  inflating: great_author/adequate_books/44578.txt.utf-8  
  inflating: great_author/adequate_books/46804-0.txt  
   creating: great_author/adequate_books/more_books/
   creating: great_author/adequate_books/more_books/.secret/
   creating: great_author/adequate_books/more_books/.secret/deeper_secrets/
   creating: great_author/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/
 extracting: great_author/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/Oliver_Twist.txt  
  inflating: great_author/adequate_books/more_books/1023.txt.utf-8  
   creating: great_author/satisfactory_books/
  inflating: great_author/satisfactory_books/16021.txt.utf-8  
   creating: great_author/satisfactory_books/more_books/
  inflating: great_author/satisfactory_books/more_books/37121.txt.utf-8  
  inflating: great_author/satisfactory_books/23765.txt.utf-8  
   creating: great_author/acceptable_books/
  inflating: great_author/acceptable_books/17879.txt.utf-8  
  inflating: great_author/acceptable_books/17880.txt.utf-8  
   creating: great_author/acceptable_books/more_books/
  inflating: great_author/acceptable_books/more_books/40723.txt.utf-8  
                                                                                
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/MetaRedPeru/find flag]
└─$ ls
great_author  great_author.zip
                                                                                
┌──(espasandia24㉿kali)-[~/Escritorio/HakinKali/MetaRedPeru/find flag]
└─$ cd great_author 
                                                                                
┌──(espasandia24㉿kali)-[~/…/HakinKali/MetaRedPeru/find flag/great_author]
└─$ ls
13771.txt.utf-8  acceptable_books  satisfactory_books
14789.txt.utf-8  adequate_books

┌──(espasandia24㉿kali)-[~/…/HakinKali/MetaRedPeru/find flag/great_author]
└─$ ls -all            
total 1936
drwxrwx--- 1 root vboxsf    4096 oct  5 22:03 .
drwxrwx--- 1 root vboxsf       0 nov  7 23:20 ..
-rwxrwx--- 1 root vboxsf 1003806 may  6  2022 13771.txt.utf-8
-rwxrwx--- 1 root vboxsf  960595 may  7  2022 14789.txt.utf-8
drwxrwx--- 1 root vboxsf    4096 may 13 15:10 acceptable_books
drwxrwx--- 1 root vboxsf       0 oct  5 22:03 adequate_books
drwxrwx--- 1 root vboxsf    4096 nov  7 23:32 satisfactory_books
                                                                                
┌──(espasandia24㉿kali)-[~/…/HakinKali/MetaRedPeru/find flag/great_author]
└─$ cd adequate_books  
                                                                                
┌──(espasandia24㉿kali)-[~/…/MetaRedPeru/find flag/great_author/adequate_books]
└─$ ls -all
total 3920
drwxrwx--- 1 root vboxsf       0 oct  5 22:03 .
drwxrwx--- 1 root vboxsf    4096 oct  5 22:03 ..
-rwxrwx--- 1 root vboxsf 1988669 abr 20  2022 44578.txt.utf-8
-rwxrwx--- 1 root vboxsf 2017890 sep  7  2014 46804-0.txt
drwxrwx--- 1 root vboxsf       0 oct  5 22:02 more_books
                                                                                
┌──(espasandia24㉿kali)-[~/…/MetaRedPeru/find flag/great_author/adequate_books]
└─$ cd more_books    
                                                                                
┌──(espasandia24㉿kali)-[~/…/find flag/great_author/adequate_books/more_books]
└─$ ls -all
total 1956
drwxrwx--- 1 root vboxsf       0 oct  5 22:02 .
drwxrwx--- 1 root vboxsf       0 oct  5 22:03 ..
-rwxrwx--- 1 root vboxsf 2001199 may  1  2022 1023.txt.utf-8
drwxrwx--- 1 root vboxsf       0 may 13 15:14 .secret
                                                                                
┌──(espasandia24㉿kali)-[~/…/find flag/great_author/adequate_books/more_books]
└─$ cd .secret   
                                                                                
┌──(espasandia24㉿kali)-[~/…/great_author/adequate_books/more_books/.secret]
└─$ ls -all
total 0
drwxrwx--- 1 root vboxsf 0 may 13 15:14 .
drwxrwx--- 1 root vboxsf 0 oct  5 22:02 ..
drwxrwx--- 1 root vboxsf 0 may 13 15:15 deeper_secrets
                                                                                
┌──(espasandia24㉿kali)-[~/…/great_author/adequate_books/more_books/.secret]
└─$ cd deeper_secrets 
                                                                                
┌──(espasandia24㉿kali)-[~/…/adequate_books/more_books/.secret/deeper_secrets]
└─$ ls -all
total 0
drwxrwx--- 1 root vboxsf 0 may 13 15:15 .
drwxrwx--- 1 root vboxsf 0 may 13 15:14 ..
drwxrwx--- 1 root vboxsf 0 oct  5 22:08 deepest_secrets
                                                                                
┌──(espasandia24㉿kali)-[~/…/adequate_books/more_books/.secret/deeper_secrets]
└─$ cd deepest_secrets 
                                                                                
┌──(espasandia24㉿kali)-[~/…/more_books/.secret/deeper_secrets/deepest_secrets]
└─$ ls -all
total 1
drwxrwx--- 1 root vboxsf  0 oct  5 22:08 .
drwxrwx--- 1 root vboxsf  0 may 13 15:15 ..
-rwxrwx--- 1 root vboxsf 23 oct  5 22:06 Oliver_Twist.txt
                                                                                
┌──(espasandia24㉿kali)-[~/…/more_books/.secret/deeper_secrets/deepest_secrets]
└─$ cat Oliver_Twist.txt                  
fl@g{Ch@rRl3$_D1cK3N$}


```
**Notas Adicionales**