import os

import mmap

def memory_map(filename, access=mmap.ACCESS_READ):
	size = os.path.getsize(filename)
	fd = os.open(filename, os.O_RDONLY)
	return mmap.mmap(fd, size, access=access)

with memory_map("rev_this") as bin_file:
	for i in range(8):
		print(chr(bin_file[i]), end = '')
	for i in range(8, 23):
		if (i & 1) == 0:
			print(chr(bin_file[i] - 5), end = '')
		else:
			print(chr(bin_file[i] + 2), end = '')
	print (chr(bin_file[23]))
