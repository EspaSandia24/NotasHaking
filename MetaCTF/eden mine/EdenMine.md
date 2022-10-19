# CTF META
## Objetivo

I downloaded one of my friend's files that describe how **frequently** he visits the "eden mine" in Zacatecas, México, but i think there might be more to it.

The most important time of the "eden mine" was during the XVII and XVIII centuries when production was mainly based in silver and gold. Given the floods in its shafts and how close it is to the city, in 1960 the exploitation of the mine ended, a little after it was adapted for tourism, being the most visited mine in the country by national and foreign tourists.



## Pistas
## Solucion


┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $ls
'edenmine.txt?token=eyJ1c2VyX2lkIjoxODgzLCJ0ZWFtX2lkIjo1MDYsImZpbGVfaWQiOjE0fQ.Y092Eg.1p5D_W71OGDRsWIcDxk-CLANt4k'

┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $mv edenmine.txt\?token\=eyJ1c2VyX2lkIjoxODgzLCJ0ZWFtX2lkIjo1MDYsImZpbGVfaWQiOjE0fQ.Y092Eg.1p5D_W71OGDRsWIcDxk-CLANt4k edenmine.txt
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt 
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggghhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiijjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssstttttttttttttttttttttttttttttttttttttttttttttttttttuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'a' | wc -l
102
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'b' | wc -l
108
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'c' | wc -l
97
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'd' | wc -l
103
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'e' | wc -l
77
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'f' | wc -l
88
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'g' | wc -l
123
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'h' | wc -l
73
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'i' | wc -l
95
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'j' | wc -l
49
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'k' | wc -l
48
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'l' | wc -l
118
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'm' | wc -l
51
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'n' | wc -l
95
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'o' | wc -l
102
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'p' | wc -l
114
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'q' | wc -l
51
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'r' | wc -l
113
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 's' | wc -l
117
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 't' | wc -l
51
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'u' | wc -l
110
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'v' | wc -l
99
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'w' | wc -l
105
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'x' | wc -l
101
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'y' | wc -l
115
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'z' | wc -l
95
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'A' | wc -l
88
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'B' | wc -l
68
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $cat edenmine.txt | grep -o 'C' | wc -l
125
┌─[oscar@oscar-parrot]─[~/CTFMETA/crypto/EdenMine]
└──╼ $

*Se decodifica From decimal en CyberChef todos los valores obtenido
		captura
*
![[Captura.PNG]]
flagMX{I_10v3_fr3qu3ncies_XD}


## Notas adicionales
## Referencias