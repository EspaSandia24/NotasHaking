**Bandit **

**Objetivo**
Hay un repositorio de git en `ssh://bandit30-git@localhost/home/bandit30-git/repo`. La contraseña para el usuario `bandit30-git`es la misma que para el usuario `bandit30`.

Clona el repositorio y encuentra la contraseña para el siguiente nivel.

**Datos de acceso**
server: **bandit.labs.overthewire.org** 
usuario: **bandit30**
contraseña: xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS

**Solucion**
```bash
bandit30@bandit:~$ cd tmp
-bash: cd: tmp: No such file or directory
bandit30@bandit:~$ cd /tmp
bandit30@bandit:/tmp$ mkdir ana
mkdir: cannot create directory ‘ana’: File exists
bandit30@bandit:/tmp$ mkdir sandiaAna
bandit30@bandit:/tmp$ cd sandiaAna
bandit30@bandit:/tmp/sandiaAna$ cd repo
bandit30@bandit:/tmp/sandiaAna/repo$ cat README.md
just an epmty file... muahaha
bandit30@bandit:/tmp/sandiaAna/repo$ git log
commit a325f29e1cc26b0f0dc5f89b4348e389b408cc87 (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Sep 1 06:30:28 2022 +0000

    initial commit of README.md
bandit30@bandit:/tmp/sandiaAna/repo$ git show a325f29e1cc26b0f0dc5f89b4348e389b408cc87
commit a325f29e1cc26b0f0dc5f89b4348e389b408cc87 (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Sep 1 06:30:28 2022 +0000

    initial commit of README.md

diff --git a/README.md b/README.md
new file mode 100644
index 0000000..029ba42
--- /dev/null
+++ b/README.md
@@ -0,0 +1 @@
+just an epmty file... muahaha
bandit30@bandit:/tmp/sandiaAna/repo$ git reflog
a325f29 (HEAD -> master, origin/master, origin/HEAD) HEAD@{0}: clone: from ssh://localhost:2220/home/bandit30-git/repo
bandit30@bandit:/tmp/sandiaAna/repo$ cd .git
bandit30@bandit:/tmp/sandiaAna/repo/.git$ ls
branches  config  description  HEAD  hooks  index  info  logs  objects  packed-refs  refs
bandit30@bandit:/tmp/sandiaAna/repo/.git$ cat packed-refs
# pack-refs with: peeled fully-peeled sorted
a325f29e1cc26b0f0dc5f89b4348e389b408cc87 refs/remotes/origin/master
831aac2e2341f009e40e46392a4f5dd318483019 refs/tags/secret
bandit30@bandit:/tmp/sandiaAna/repo/.git$ git show 831aac2e2341f009e40e46392a4f5dd318483019
OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt

```
**Notas adicionales** 

**Referencias** 
