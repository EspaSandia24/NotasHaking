**Descripcion**

This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](https://jupiter.challenges.picoctf.org/static/a648ca6dd275b9454c5d0de6d0f6efd3/VaultDoor3.java)

**Solucion**
```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/vault-door-3]
└─$ ls 
'vault door 3.md'   VaultDoor3.java
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/reversing/vault-door-3]
└─$ cat VaultDoor3.java 
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
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

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18gb41_u_4_mfr340");
    }
}

```
![[Pasted image 20221115090128.png]]
jU5t_a_s1mpl3_an4gr4m_4_u_1fb380
```bash
C:\Users\crist\Documents\Haking\retos Pico CTF\2019\reversing\vault-door-3>javac VaultDoor3.java

C:\Users\crist\Documents\Haking\retos Pico CTF\2019\reversing\vault-door-3>java VaultDoor3
Enter vault password: jU5t_a_s1mpl3_an4gr4m_4_u_1fb380
Access denied!

C:\Users\crist\Documents\Haking\retos Pico CTF\2019\reversing\vault-door-3>java VaultDoor3
Enter vault password: picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_1fb380}
Access granted.

C:\Users\crist\Documents\Haking\retos Pico CTF\2019\reversing\vault-door-3>
```
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_1fb380}
**Notas Adicionales **