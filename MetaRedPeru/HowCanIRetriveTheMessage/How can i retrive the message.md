# Crypto
## Objetivo
Consider an RSA that is using twin primes. IF=10403 and e=8743. Show how the adversary can recover the message corresponding to c=99
## Pistas
## Solucion
┌─[✗]─[oscar@oscar-parrot]─[~/Metaredperu/cripto/HowCanIRetriveTheMessage]
└──╼ $cd /opt/RsaCtfTool/
┌─[oscar@oscar-parrot]─[/opt/RsaCtfTool]
└──╼ $python3 RsaCtfTool.py -e=8743 -n=10403 --uncipher 99
private argument is not set, the private key will not be displayed, even if recovered.

[*] Testing key /tmp/tmpf3ow3ts8.
attack initialized...
[*] Performing factordb attack on /tmp/tmpf3ow3ts8.
[*] Attack success with factordb method !

Results for /tmp/tmpf3ow3ts8:

Unciphered data :
HEX : 0x2496
		*Solucion								INT (big endian) : 9366
INT (little endian) : 38436
utf-16 : 阤
STR : b'$\x96'
HEX : 0x2496
INT (big endian) : 9366
INT (little endian) : 38436
utf-16 : 阤
STR : b'$\x96'
┌─[oscar@oscar-parrot]─[/opt/RsaCtfTool]
└──╼ $


Flag = 9366

## Notas adicionales
## Referencias 

