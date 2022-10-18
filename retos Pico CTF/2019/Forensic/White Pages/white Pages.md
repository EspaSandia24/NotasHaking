**Descripcion**



**Solucion**
```bash
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/White Pages]
└─$ ls    
'white Pages.md'   whitepages.txt
                                                                                                                               
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/White Pages]
└─$ file whitepages.txt 
whitepages.txt: Unicode text, UTF-8 text, with very long lines (1376), with no line terminators
                                                                                                                               
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/White Pages]
└─$ xxd whitepages.txt|head
00000000: e280 83e2 8083 e280 83e2 8083 20e2 8083  ............ ...
00000010: 20e2 8083 e280 83e2 8083 e280 83e2 8083   ...............
00000020: 20e2 8083 e280 8320 e280 83e2 8083 e280   ...... ........
00000030: 83e2 8083 20e2 8083 e280 8320 e280 8320  .... ...... ... 
00000040: 2020 e280 83e2 8083 e280 83e2 8083 e280    ..............
00000050: 8320 20e2 8083 20e2 8083 e280 8320 e280  .  ... ...... ..
00000060: 8320 20e2 8083 e280 83e2 8083 2020 e280  .  .........  ..
00000070: 8320 20e2 8083 2020 2020 e280 8320 e280  .  ...    ... ..
00000080: 83e2 8083 e280 83e2 8083 2020 e280 8320  ..........  ... 
00000090: e280 8320 e280 8320 e280 83e2 8083 e280  ... ... ........
                                                                                                                               
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/White Pages]
└─$ python -c "import pwntools"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'pwntools'
                                                                                                                       
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/White Pages]
└─$ python3 -m pip install pwntools
Defaulting to user installation because normal site-packages is not writeable
Collecting pwntools
  Downloading pwntools-4.8.0-py2.py3-none-any.whl (11.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.7/11.7 MB 2.2 MB/s eta 0:00:00
Requirement already satisfied: python-dateutil in /usr/lib/python3/dist-packages (from pwntools) (2.8.1)
Requirement already satisfied: six>=1.12.0 in /usr/lib/python3/dist-packages (from pwntools) (1.16.0)
Collecting psutil>=3.3.0
  Downloading psutil-5.9.2-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (282 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 282.8/282.8 kB 113.6 kB/s eta 0:00:00
Collecting rpyc
  Downloading rpyc-5.2.3-py3-none-any.whl (71 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 71.3/71.3 kB 587.3 kB/s eta 0:00:00
Collecting pyelftools>=0.2.4
  Downloading pyelftools-0.29-py2.py3-none-any.whl (174 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 174.3/174.3 kB 1.2 MB/s eta 0:00:00
Requirement already satisfied: paramiko>=1.15.2 in /usr/lib/python3/dist-packages (from pwntools) (2.10.4)
Collecting ropgadget>=5.3
  Downloading ROPGadget-7.1-py3-none-any.whl (31 kB)
Requirement already satisfied: pygments>=2.0 in /usr/lib/python3/dist-packages (from pwntools) (2.12.0)
Collecting unicorn>=1.0.2rc1
  Downloading unicorn-2.0.0-py2.py3-none-manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.1/16.1 MB 1.6 MB/s eta 0:00:00
Requirement already satisfied: sortedcontainers in /usr/lib/python3/dist-packages (from pwntools) (2.4.0)
Requirement already satisfied: pysocks in /usr/lib/python3/dist-packages (from pwntools) (1.7.1)
Requirement already satisfied: mako>=1.0.0 in /usr/lib/python3/dist-packages (from pwntools) (1.1.3)
Collecting pathlib2
  Downloading pathlib2-2.3.7.post1-py2.py3-none-any.whl (18 kB)
Collecting colored-traceback
  Downloading colored-traceback-0.3.0.tar.gz (3.8 kB)
  Preparing metadata (setup.py) ... done
Collecting intervaltree>=3.0
  Downloading intervaltree-3.1.0.tar.gz (32 kB)
  Preparing metadata (setup.py) ... done
Requirement already satisfied: requests>=2.0 in /usr/lib/python3/dist-packages (from pwntools) (2.27.1)
Requirement already satisfied: packaging in /usr/lib/python3/dist-packages (from pwntools) (21.3)
Collecting capstone>=3.0.5rc2
  Downloading capstone-5.0.0rc2-py3-none-manylinux1_x86_64.manylinux_2_5_x86_64.whl (2.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.8/2.8 MB 4.0 MB/s eta 0:00:00
Requirement already satisfied: pip>=6.0.8 in /usr/lib/python3/dist-packages (from pwntools) (22.2)
Requirement already satisfied: pyserial>=2.7 in /usr/lib/python3/dist-packages (from pwntools) (3.5)
Collecting plumbum
  Downloading plumbum-1.8.0-py3-none-any.whl (117 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 117.5/117.5 kB 1.2 MB/s eta 0:00:00
Building wheels for collected packages: intervaltree, colored-traceback
  Building wheel for intervaltree (setup.py) ... done
  Created wheel for intervaltree: filename=intervaltree-3.1.0-py2.py3-none-any.whl size=26119 sha256=fb127b334b44920546f2cba93f79884dd8358a2cabd26123863655b77da8089f
  Stored in directory: /home/espasandia24/.cache/pip/wheels/fa/80/8c/43488a924a046b733b64de3fac99252674c892a4c3801c0a61
  Building wheel for colored-traceback (setup.py) ... done
  Created wheel for colored-traceback: filename=colored_traceback-0.3.0-py3-none-any.whl size=4622 sha256=b71c7779bdadf6ba775186c60e716df17c805dc9f204ad1387af91584b8d56de
  Stored in directory: /home/espasandia24/.cache/pip/wheels/10/49/bd/750e09783fb038570efede2d03819a7141fc2350de51daf575
Successfully built intervaltree colored-traceback
Installing collected packages: unicorn, pyelftools, psutil, plumbum, pathlib2, intervaltree, colored-traceback, capstone, rpyc, ropgadget, pwntools
  WARNING: The scripts rpyc_classic, rpyc_classic.py, rpyc_registry and rpyc_registry.py are installed in '/home/espasandia24/.local/bin' which is not on PATH.                                                                               
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.    
  WARNING: The scripts asm, checksec, common, constgrep, cyclic, debug, disablenx, disasm, elfdiff, elfpatch, errno, hex, main, phd, pwn, pwnstrip, scramble, shellcraft, template, unhex, update and version are installed in '/home/espasandia24/.local/bin' which is not on PATH.                                                                                 
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.    
Successfully installed capstone-5.0.0rc2 colored-traceback-0.3.0 intervaltree-3.1.0 pathlib2-2.3.7.post1 plumbum-1.8.0 psutil-5.9.2 pwntools-4.8.0 pyelftools-0.29 ropgadget-7.1 rpyc-5.2.3 unicorn-2.0.0
                                                                                                                       
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/White Pages]
└─$ python -c "import pwntools"    
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'pwntools'
                                                                                                                       
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/White Pages]
└─$ sudo python3 -m pip install pwntools
[sudo] contraseña para espasandia24: 
Collecting pwntools
  Downloading pwntools-4.8.0-py2.py3-none-any.whl (11.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.7/11.7 MB 967.3 kB/s eta 0:00:00
Requirement already satisfied: six>=1.12.0 in /usr/lib/python3/dist-packages (from pwntools) (1.16.0)
Requirement already satisfied: packaging in /usr/lib/python3/dist-packages (from pwntools) (21.3)
Collecting psutil>=3.3.0
  Downloading psutil-5.9.2-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (282 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 282.8/282.8 kB 1.2 MB/s eta 0:00:00
Collecting unicorn>=1.0.2rc1
  Downloading unicorn-2.0.0-py2.py3-none-manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.1/16.1 MB 1.4 MB/s eta 0:00:00
Requirement already satisfied: sortedcontainers in /usr/lib/python3/dist-packages (from pwntools) (2.4.0)
Collecting colored-traceback
  Downloading colored-traceback-0.3.0.tar.gz (3.8 kB)
  Preparing metadata (setup.py) ... done
Requirement already satisfied: requests>=2.0 in /usr/lib/python3/dist-packages (from pwntools) (2.27.1)
Collecting ropgadget>=5.3
  Downloading ROPGadget-7.1-py3-none-any.whl (31 kB)
Requirement already satisfied: python-dateutil in /usr/lib/python3/dist-packages (from pwntools) (2.8.1)
Collecting intervaltree>=3.0
  Downloading intervaltree-3.1.0.tar.gz (32 kB)
  Preparing metadata (setup.py) ... done
Requirement already satisfied: pygments>=2.0 in /usr/lib/python3/dist-packages (from pwntools) (2.12.0)
Requirement already satisfied: mako>=1.0.0 in /usr/lib/python3/dist-packages (from pwntools) (1.1.3)
Requirement already satisfied: pyserial>=2.7 in /usr/lib/python3/dist-packages (from pwntools) (3.5)
Collecting pathlib2
  Downloading pathlib2-2.3.7.post1-py2.py3-none-any.whl (18 kB)
Collecting pyelftools>=0.2.4
  Downloading pyelftools-0.29-py2.py3-none-any.whl (174 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 174.3/174.3 kB 1.9 MB/s eta 0:00:00
Collecting capstone>=3.0.5rc2
  Downloading capstone-5.0.0rc2-py3-none-manylinux1_x86_64.manylinux_2_5_x86_64.whl (2.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.8/2.8 MB 2.4 MB/s eta 0:00:00
Requirement already satisfied: pysocks in /usr/lib/python3/dist-packages (from pwntools) (1.7.1)
Requirement already satisfied: pip>=6.0.8 in /usr/lib/python3/dist-packages (from pwntools) (22.2)
Requirement already satisfied: paramiko>=1.15.2 in /usr/lib/python3/dist-packages (from pwntools) (2.10.4)
Collecting rpyc
  Downloading rpyc-5.2.3-py3-none-any.whl (71 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 71.3/71.3 kB 1.0 MB/s eta 0:00:00
Collecting plumbum
  Downloading plumbum-1.8.0-py3-none-any.whl (117 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 117.5/117.5 kB 1.2 MB/s eta 0:00:00
Building wheels for collected packages: intervaltree, colored-traceback
  Building wheel for intervaltree (setup.py) ... done
  Created wheel for intervaltree: filename=intervaltree-3.1.0-py2.py3-none-any.whl size=26119 sha256=23baa5951264898ce0f35a24e1d3b33c1cfe9ccb207dfb08f7ff02f02a584b77
  Stored in directory: /root/.cache/pip/wheels/fa/80/8c/43488a924a046b733b64de3fac99252674c892a4c3801c0a61
  Building wheel for colored-traceback (setup.py) ... done
  Created wheel for colored-traceback: filename=colored_traceback-0.3.0-py3-none-any.whl size=4622 sha256=a94633f96e5dfd982b970cb05f7621dd8e1861a6fdebedff5416f7d5d2500709
  Stored in directory: /root/.cache/pip/wheels/10/49/bd/750e09783fb038570efede2d03819a7141fc2350de51daf575
Successfully built intervaltree colored-traceback
Installing collected packages: unicorn, pyelftools, psutil, plumbum, pathlib2, intervaltree, colored-traceback, capstone, rpyc, ropgadget, pwntools
Successfully installed capstone-5.0.0rc2 colored-traceback-0.3.0 intervaltree-3.1.0 pathlib2-2.3.7.post1 plumbum-1.8.0 psutil-5.9.2 pwntools-4.8.0 pyelftools-0.29 ropgadget-7.1 rpyc-5.2.3 unicorn-2.0.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv                 
                                                                                                                       
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/White Pages]
└─$ python -c "import pwntools"         
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'pwntools'
                                                                                                                       
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/White Pages]
└─$ python3                        
Python 3.10.5 (main, Jun  8 2022, 09:26:22) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pwntools
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'pwntools'
>>> from pwn import *
>>>  exit
File "<stdin>", line 1
    exit
IndentationError: unexpected indent
>>> ext
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ext' is not defined
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> ^B
zsh: suspended  python3
                                                                                                                       
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/White Pages]
└─$  nano exp.py
                                                                                                                       
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/White Pages]
└─$ python3 exp.py                
Traceback (most recent call last):
  File "/home/espasandia24/Escritorio/HakinKali/retos Pico CTF/2019/Forensic/White Pages/exp.py", line 5, in <module>
    data = data.replace('\x20',b'1')
TypeError: a bytes-like object is required, not 'str'
                                                                                                                       
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/White Pages]
└─$ nano exp.py     
                                                                                                                       
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/White Pages]
└─$ python3 exp.py
b'\n\t\tpicoCTF\n\n\t\tSEE PUBLIC RECORDS & BACKGROUND REPORT\n\t\t5000 Forbes Ave, Pittsburgh, PA 15213\n\t\tpicoCTF{not_all_spaces_are_created_equal_c54f27cd05c2189f8147cc6f5deb2e56}\n\t\t'
                                                                                                                       
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/White Pages]
└─$ 


```
picoCTF{not_all_spaces_are_created_equal_c54f27cd05c2189f8147cc6f5deb2e56}
**Notas Adicionales**