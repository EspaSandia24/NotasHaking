import string

cadena = 'dspttjohuifsvcjdpoabrkttds' 
letras = string.ascii_letters
rot = 25
flag = ''

for c in cadena:
	flag += letras[(letras.find(c)+rot)%26]

print(flag)
