datos = open('message.txt').read().strip().split(' ')

datos = [int(i)%37 for i in datos]

flag= ''
for n in datos:
	if n in range(26):
		flag += chr(n+65)
	elif n in range(26,36):
		flag += chr(n+22)
	else:
		flag += "_"
print(flag)
