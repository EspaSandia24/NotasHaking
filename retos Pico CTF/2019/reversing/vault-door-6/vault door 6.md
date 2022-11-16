**Descripcion**

This vault uses an XOR encryption scheme. The source code for this vault is here: [VaultDoor6.java](https://jupiter.challenges.picoctf.org/static/cdb33ffba609e2521797aac66320ec65/VaultDoor6.java)

**Solucion**
```bash
─(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/vault-door-6]
└─$ wget https://jupiter.challenges.picoctf.org/static/cdb33ffba609e2521797aac66320ec65/VaultDoor6.java
--2022-11-16 13:32:34--  https://jupiter.challenges.picoctf.org/static/cdb33ffba609e2521797aac66320ec65/VaultDoor6.java
Resolviendo jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Conectando con jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)[3.131.60.8]:443... conectado.
Petición HTTP enviada, esperando respuesta... 200 OK
Longitud: 1526 (1.5K) [application/octet-stream]
Grabando a: «VaultDoor6.java»

VaultDoor6.java     100%[===================>]   1.49K  --.-KB/s    en 0.001s  

2022-11-16 13:32:35 (1.45 MB/s) - «VaultDoor6.java» guardado [1526/1526]

                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/vault-door-6]
└─$ ls
'vault door 6.md'   VaultDoor6.java
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/vault-door-6]
└─$ cat VaultDoor6.java
import java.util.*;

class VaultDoor6 {
    public static void main(String args[]) {
        VaultDoor6 vaultDoor = new VaultDoor6();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
        String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
        if (vaultDoor.checkPassword(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
    }

    // Dr. Evil gave me a book called Applied Cryptography by Bruce Schneier,
    // and I learned this really cool encryption system. This will be the
    // strongest vault door in Dr. Evil's entire evil volcano compound for sure!
    // Well, I didn't exactly read the *whole* book, but I'm sure there's
    // nothing important in the last 750 pages.
    //
    // -Minion #3091
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x6c, 0x60, 0x37, 0x30, 0x60, 0x31, 0x36,
        };
        for (int i=0; i<32; i++) {
            if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
                return false;
            }
        }
        return true;
    }
}
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/vault-door-6]
└─$ 

```
	analizamos el codigo y podemos ver que la bandera esta incriptada  abrimos python y hqcemos lo siguiente
```bash
┌──(espasandia24㉿kali)-[~]
└─$ python3           
Python 3.10.5 (main, Jun  8 2022, 09:26:22) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> myBytes= [0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
...             0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
...             0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
...             0xa , 0x6c, 0x60, 0x37, 0x30, 0x60, 0x31, 0x36]
>>> myBytes
[59, 101, 33, 10, 56, 0, 54, 29, 10, 61, 97, 39, 17, 102, 39, 10, 33, 29, 97, 59, 10, 45, 101, 39, 10, 108, 96, 55, 48, 96, 49, 54]
>>> flag=[i ^ 0x55 for i in myBytes]
>>> flag
[110, 48, 116, 95, 109, 85, 99, 72, 95, 104, 52, 114, 68, 51, 114, 95, 116, 72, 52, 110, 95, 120, 48, 114, 95, 57, 53, 98, 101, 53, 100, 99]
>>> flag=[chr(i) for i in flag]
>>> flag
['n', '0', 't', '_', 'm', 'U', 'c', 'H', '_', 'h', '4', 'r', 'D', '3', 'r', '_', 't', 'H', '4', 'n', '_', 'x', '0', 'r', '_', '9', '5', 'b', 'e', '5', 'd', 'c']
>>> ''.join(flag)
'n0t_mUcH_h4rD3r_tH4n_x0r_95be5dc'
>>> 

```
picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_95be5dc}
**Notas Adicionales**