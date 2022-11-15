**Descripcion**

This vault uses ASCII encoding for the password. The source code for this vault is here: [VaultDoor4.java](https://jupiter.challenges.picoctf.org/static/09d3002ae349631324a17e2255ae8df2/VaultDoor4.java)

**Solucion**
```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/vault-door-3]
└─$ ls 
'vault door 3.md'   VaultDoor3.class   VaultDoor3.java
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/vault-door-3]
└─$ cd ..          
                                                                                
┌──(espasandia24㉿kali)-[~/…/HakinKali/retos Pico CTF/2019/reversing]
└─$ ls
asm1  asm3  Bill_gat35  vault-6       vault-door-3  vault-door-traing
asm2  asm4  vault-5     vault-door-1  vault-door-4
                                                                                
┌──(espasandia24㉿kali)-[~/…/HakinKali/retos Pico CTF/2019/reversing]
└─$ cd vault-door-4
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/vault-door-4]
└─$ ls
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/vault-door-4]
└─$ wget https://jupiter.challenges.picoctf.org/static/09d3002ae349631324a17e2255ae8df2/VaultDoor4.java
--2022-11-15 09:06:59--  https://jupiter.challenges.picoctf.org/static/09d3002ae349631324a17e2255ae8df2/VaultDoor4.java
Resolviendo jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Conectando con jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)[3.131.60.8]:443... conectado.
Petición HTTP enviada, esperando respuesta... 200 OK
Longitud: 1497 (1.5K) [application/octet-stream]
Grabando a: «VaultDoor4.java»

VaultDoor4.java     100%[===================>]   1.46K  --.-KB/s    en 0.002s  

2022-11-15 09:07:15 (725 KB/s) - «VaultDoor4.java» guardado [1497/1497]

                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/vault-door-4]
└─$ ls
'valut door 4.md'   VaultDoor4.java
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/vault-door-4]
└─$ cat VaultDoor4.java 
import java.util.*;

class VaultDoor4 {
    public static void main(String args[]) {
        VaultDoor4 vaultDoor = new VaultDoor4();
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

    // I made myself dizzy converting all of these numbers into different bases,
    // so I just *know* that this vault will be impenetrable. This will make Dr.
    // Evil like me better than all of the other minions--especially Minion
    // #5620--I just know it!
    //
    //  .:::.   .:::.
    // :::::::.:::::::
    // :::::::::::::::
    // ':::::::::::::'
    //   ':::::::::'
    //     ':::::'
    //       ':'
    // -Minion #7781
    public boolean checkPassword(String password) {
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 0143, 061 ,
            '9' , '4' , 'f' , '7' , '4' , '5' , '8' , 'e' ,
        };
        for (int i=0; i<32; i++) {
            if (passBytes[i] != myBytes[i]) {
                return false;
            }
        }
        return true;
    }
}
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/vault-door-4]
└─$ 

```
![[Pasted image 20221115091330.png]]

"jU5t_4_bUnCh_0f_bYt3s_c194f7458e"
```bash
C:\Users\crist\Documents\Haking\retos Pico CTF\2019\reversing\vault-door-4>javac VaultDoor4.java

C:\Users\crist\Documents\Haking\retos Pico CTF\2019\reversing\vault-door-4>java VaultDoor4
Enter vault password: picoCTF{jU5t_4_bUnCh_0f_bYt3s_c194f7458e}
Access granted.

C:\Users\crist\Documents\Haking\retos Pico CTF\2019\reversing\vault-door-4>
```

picoCTF{jU5t_4_bUnCh_0f_bYt3s_c194f7458e}