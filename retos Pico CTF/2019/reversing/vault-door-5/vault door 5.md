**Descripcion**

In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! The source code for this vault is here: [VaultDoor5.java](https://jupiter.challenges.picoctf.org/static/0a53bf0deaba6919f98d8550c35aa253/VaultDoor5.java)

**Solucion**
```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/vault-door-5]
└─$ wget https://jupiter.challenges.picoctf.org/static/0a53bf0deaba6919f98d8550c35aa253/VaultDoor5.java
--2022-11-16 13:00:54--  https://jupiter.challenges.picoctf.org/static/0a53bf0deaba6919f98d8550c35aa253/VaultDoor5.java
Resolviendo jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Conectando con jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)[3.131.60.8]:443... conectado.
Petición HTTP enviada, esperando respuesta... 200 OK
Longitud: 1847 (1.8K) [application/octet-stream]
Grabando a: «VaultDoor5.java»

VaultDoor5.java     100%[===================>]   1.80K  --.-KB/s    en 0.004s  

2022-11-16 13:00:56 (506 KB/s) - «VaultDoor5.java» guardado [1847/1847]

                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/vault-door-5]
└─$ ls
'vault door 5.md'   VaultDoor5.java
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/vault-door-5]
└─$ cat VaultDoor5.java 
import java.net.URLDecoder;
import java.util.*;

class VaultDoor5 {
    public static void main(String args[]) {
        VaultDoor5 vaultDoor = new VaultDoor5();
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

    // Minion #7781 used base 8 and base 16, but this is base 64, which is
    // like... eight times stronger, right? Riiigghtt? Well that's what my twin
    // brother Minion #2415 says, anyway.
    //
    // -Minion #2414
    public String base64Encode(byte[] input) {
        return Base64.getEncoder().encodeToString(input);
    }

    // URL encoding is meant for web pages, so any double agent spies who steal
    // our source code will think this is a web site or something, defintely not
    // vault door! Oh wait, should I have not said that in a source code
    // comment?
    //
    // -Minion #2415
    public String urlEncode(byte[] input) {
        StringBuffer buf = new StringBuffer();
        for (int i=0; i<input.length; i++) {
            buf.append(String.format("%%%2x", input[i]));
        }
        return buf.toString();
    }

    public boolean checkPassword(String password) {
        String urlEncoded = urlEncode(password.getBytes());
        String base64Encoded = base64Encode(urlEncoded.getBytes());
        String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
                        + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
                        + "JTM0JTVmJTMwJTYyJTM5JTM1JTM3JTYzJTM0JTY2";
        return base64Encoded.equals(expected);
    }
}
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/vault-door-5]
└─$ 

```
checamos el codigo y vemos la variable exected que es la que contiene la bansera.
vamos a  cyberchef donde ddecodificamos en base64 y luego en url y nos da la bandera
![[Pasted image 20221116132333.png]]

picoCTF{c0nv3rt1ng_fr0m_ba5e_64_0b957c4f}

![[Pasted image 20221116132824.png]]
**Notas Adicionales**
https://gchq.github.io/CyberChef