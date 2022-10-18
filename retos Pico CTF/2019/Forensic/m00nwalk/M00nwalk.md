**Descripcion**
Decode this [message](https://jupiter.challenges.picoctf.org/static/d6fcea5e3c6433680ea4f914e24fab61/message.wav) from the moon.


**Solucion**
```bash
──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/m00nwalk]
└─$ ls 
M00nwalk.md  message.wav
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/m00nwalk]
└─$ file message.wav 
message.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 48000 Hz
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/m00nwalk]
└─$ open message.wav  
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/m00nwalk]
└─$ cd opt/
cd: no existe el fichero o el directorio: opt/
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/m00nwalk]
└─$ cd \opt
cd: no existe el fichero o el directorio: opt
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/m00nwalk]
└─$ cd /opt                
                                                                                
┌──(espasandia24㉿kali)-[/opt]
└─$ sudo git clone https://github.com/colaclanth/sstv.git
[sudo] contraseña para espasandia24: 
Clonando en 'sstv'...
remote: Enumerating objects: 221, done.
remote: Total 221 (delta 0), reused 0 (delta 0), pack-reused 221
Recibiendo objetos: 100% (221/221), 1.01 MiB | 377.00 KiB/s, listo.
Resolviendo deltas: 100% (140/140), listo.
                                                                                
┌──(espasandia24㉿kali)-[/opt]
└─$ cd sstv 
┌──(espasandia24㉿kali)-[/opt/sstv]
└─$ sudo python3 setup.py install       
running install
/usr/lib/python3/dist-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
  warnings.warn(
/usr/lib/python3/dist-packages/setuptools/command/easy_install.py:158: EasyInstallDeprecationWarning: easy_install command is deprecated. Use build and pip and other standards-based tools.
  warnings.warn(
running bdist_egg
running egg_info
creating sstv.egg-info
writing sstv.egg-info/PKG-INFO
writing dependency_links to sstv.egg-info/dependency_links.txt
writing entry points to sstv.egg-info/entry_points.txt
writing requirements to sstv.egg-info/requires.txt
writing top-level names to sstv.egg-info/top_level.txt
writing manifest file 'sstv.egg-info/SOURCES.txt'
reading manifest file 'sstv.egg-info/SOURCES.txt'
adding license file 'LICENSE'
writing manifest file 'sstv.egg-info/SOURCES.txt'
installing library code to build/bdist.linux-x86_64/egg
running install_lib
running build_py
creating build
creating build/lib
creating build/lib/sstv
copying sstv/common.py -> build/lib/sstv
copying sstv/__init__.py -> build/lib/sstv
copying sstv/command.py -> build/lib/sstv
copying sstv/spec.py -> build/lib/sstv
copying sstv/__main__.py -> build/lib/sstv
copying sstv/decode.py -> build/lib/sstv
creating build/bdist.linux-x86_64
creating build/bdist.linux-x86_64/egg
creating build/bdist.linux-x86_64/egg/sstv
copying build/lib/sstv/common.py -> build/bdist.linux-x86_64/egg/sstv
copying build/lib/sstv/__init__.py -> build/bdist.linux-x86_64/egg/sstv
copying build/lib/sstv/command.py -> build/bdist.linux-x86_64/egg/sstv
copying build/lib/sstv/spec.py -> build/bdist.linux-x86_64/egg/sstv
copying build/lib/sstv/__main__.py -> build/bdist.linux-x86_64/egg/sstv
copying build/lib/sstv/decode.py -> build/bdist.linux-x86_64/egg/sstv
byte-compiling build/bdist.linux-x86_64/egg/sstv/common.py to common.cpython-310.pyc
byte-compiling build/bdist.linux-x86_64/egg/sstv/__init__.py to __init__.cpython-310.pyc
byte-compiling build/bdist.linux-x86_64/egg/sstv/command.py to command.cpython-310.pyc
byte-compiling build/bdist.linux-x86_64/egg/sstv/spec.py to spec.cpython-310.pyc
byte-compiling build/bdist.linux-x86_64/egg/sstv/__main__.py to __main__.cpython-310.pyc
byte-compiling build/bdist.linux-x86_64/egg/sstv/decode.py to decode.cpython-310.pyc
creating build/bdist.linux-x86_64/egg/EGG-INFO
copying sstv.egg-info/PKG-INFO -> build/bdist.linux-x86_64/egg/EGG-INFO
copying sstv.egg-info/SOURCES.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying sstv.egg-info/dependency_links.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying sstv.egg-info/entry_points.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying sstv.egg-info/requires.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying sstv.egg-info/top_level.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
zip_safe flag not set; analyzing archive contents...
creating dist
creating 'dist/sstv-0.1-py3.10.egg' and adding 'build/bdist.linux-x86_64/egg' to it
removing 'build/bdist.linux-x86_64/egg' (and everything under it)
Processing sstv-0.1-py3.10.egg
Copying sstv-0.1-py3.10.egg to /usr/local/lib/python3.10/dist-packages
Adding sstv 0.1 to easy-install.pth file
Installing sstv script to /usr/local/bin

Installed /usr/local/lib/python3.10/dist-packages/sstv-0.1-py3.10.egg
Processing dependencies for sstv==0.1
Searching for PySoundFile
Reading https://pypi.org/simple/PySoundFile/
/usr/lib/python3/dist-packages/pkg_resources/__init__.py:116: PkgResourcesDeprecationWarning:  is an invalid version and will not be supported in a future release
  warnings.warn(
Downloading https://files.pythonhosted.org/packages/2a/b3/0b871e5fd31b9a8e54b4ee359384e705a1ca1e2870706d2f081dc7cc1693/PySoundFile-0.9.0.post1-py2.py3-none-any.whl#sha256=db14f84f4af1910f54766cf0c0f19d52414fa80aa0e11cb338b5614946f39947
Best match: PySoundFile 0.9.0.post1
Processing PySoundFile-0.9.0.post1-py2.py3-none-any.whl
Installing PySoundFile-0.9.0.post1-py2.py3-none-any.whl to /usr/local/lib/python3.10/dist-packages
Adding PySoundFile 0.9.0.post1 to easy-install.pth file

Installed /usr/local/lib/python3.10/dist-packages/PySoundFile-0.9.0.post1-py3.10.egg
Searching for scipy==1.7.3
Best match: scipy 1.7.3
Adding scipy 1.7.3 to easy-install.pth file

Using /usr/lib/python3/dist-packages
Searching for numpy==1.21.5
Best match: numpy 1.21.5
Adding numpy 1.21.5 to easy-install.pth file
Installing f2py script to /usr/local/bin
Installing f2py3 script to /usr/local/bin
Installing f2py3.10 script to /usr/local/bin

Using /usr/lib/python3/dist-packages
Searching for Pillow==9.2.0
Best match: Pillow 9.2.0
Adding Pillow 9.2.0 to easy-install.pth file

Using /usr/lib/python3/dist-packages
Searching for cffi==1.15.1
Best match: cffi 1.15.1
Adding cffi 1.15.1 to easy-install.pth file

Using /usr/lib/python3/dist-packages
Finished processing dependencies for sstv==0.1

┌──(espasandia24㉿kali)-[/opt/sstv]
└─$ cd ~   
                                                                                
┌──(espasandia24㉿kali)-[~]
└─$ cd Escritorio/HakinKali/retos\ Pico\ CTF/2019/Forensic
                                                                                
┌──(espasandia24㉿kali)-[~/…/HakinKali/retos Pico CTF/2019/Forensic]
└─$ cd m00nwalk                                           
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/m00nwalk]
└─$ sstv -d message.wav -o resultado.png     
[sstv] Searching for calibration header... Found!    
[sstv] Detected SSTV mode Scottie 1
[sstv] Decoding image...   [##############################################] 100%
[sstv] Drawing image data...
[sstv] ...Done!
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/m00nwalk]
└─$ ls              
M00nwalk.md  message.wav  resultado.png
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/m00nwalk]
└─$ open resultado.png 
                                                                                
┌──(espasandia24㉿kali)-[~/…/retos Pico CTF/2019/Forensic/m00nwalk]
└─$ 
```
![[Pasted image 20221018125719.png]]

picoCTF{beep_boop_im_in_space}
**Notas Adicionales**