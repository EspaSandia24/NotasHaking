**Descripcion**

Can you open this safe?I forgot the key to my safe but this [program](https://artifacts.picoctf.net/c/463/SafeOpener.java) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?Put the password you recover into the picoCTF flag format like:`picoCTF{password}`

**Solucion**
```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/Safe-Opener]
└─$ ls
'safe opener.md'   SafeOpener.java
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/Safe-Opener]
└─$ file SafeOpener.java 
SafeOpener.java: Java source, ASCII text
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/Safe-Opener]
└─$ cat SafeOpener.java 
import java.io.*;
import java.util.*;  
public class SafeOpener {
    public static void main(String args[]) throws IOException {
        BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
        Base64.Encoder encoder = Base64.getEncoder();
        String encodedkey = "";
        String key = "";
        int i = 0;
        boolean isOpen;
        

        while (i < 3) {
            System.out.print("Enter password for the safe: ");
            key = keyboard.readLine();

            encodedkey = encoder.encodeToString(key.getBytes());
            System.out.println(encodedkey);
              
            isOpen = openSafe(encodedkey);
            if (!isOpen) {
                System.out.println("You have  " + (2 - i) + " attempt(s) left");
                i++;
                continue;
            }
            break;
        }
    }
    
    public static boolean openSafe(String password) {
        String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";
        
        if (password.equals(encodedkey)) {
            System.out.println("Sesame open");
            return true;
        }
        else {
            System.out.println("Password is incorrect\n");
            return false;
        }
    }
}                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/Safe-Opener]
└─$ echo "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz" | base64 -d
pl3as3_l3t_m3_1nt0_th3_saf3                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Reversing/Safe-Opener]
└─$ 

```

picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}

**Notas Adicionales**