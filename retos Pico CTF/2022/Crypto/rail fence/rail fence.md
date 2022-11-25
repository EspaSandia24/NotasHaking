**Descripcion**

A type of transposition cipher is the rail fence cipher, which is described [here](https://en.wikipedia.org/wiki/Rail_fence_cipher). Here is one such cipher encrypted using the rail fence with 4 rails. Can you decrypt it? Download the message [here](https://artifacts.picoctf.net/c/273/message.txt). Put the decoded message in the picoCTF flag format, `picoCTF{decoded_message}`.

**Solucion**
```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Crypto/rail fence]
└─$ ls                
 message.txt  'rail fence.md'   Rail_fence_cipher
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Crypto/rail fence]
└─$ file message.txt  
message.txt: ASCII text, with no line terminators
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Crypto/rail fence]
└─$ cat message.txt  
Ta _7N6D8Dhlg:W3D_H3C31N__387ef sHR053F38N43DFD i33___N6                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2022/Crypto/rail fence]
└─$ 
```
![[Pasted image 20221125134252.png]]

picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_83F6D8D7}

**Notas Adicionales**
https://gchq.github.io/CyberChef/#recipe=Rail_Fence_Cipher_Decode(4,0)&input=VGEgXzdONkQ4RGhsZzpXM0RfSDNDMzFOX18zODdlZiBzSFIwNTNGMzhONDNERkQgaTMzX19fTjY
