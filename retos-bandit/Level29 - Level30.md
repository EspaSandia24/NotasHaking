**Bandit **

**Objetivo**
Hay un repositorio de git en `ssh://bandit29-git@localhost/home/bandit29-git/repo`. La contraseña para el usuario `bandit29-git`es la misma que para el usuario `bandit29`.

Clona el repositorio y encuentra la contraseña para el siguiente nivel.

**Datos de acceso**
server: **bandit.labs.overthewire.org** 
usuario: **bandit29**
contraseña: tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S

**Solucion**
```bash
bandit29@bandit:~$ cd /temp
-bash: cd: /temp: No such file or directory
bandit29@bandit:~$ cd /temp/
-bash: cd: /temp/: No such file or directory
bandit29@bandit:~$ cd /tmp
bandit29@bandit:/tmp$ mkdir sandia
mkdir: cannot create directory ‘sandia’: File exists
bandit29@bandit:/tmp$ mkdir sandias
bandit29@bandit:/tmp$ cd sandias
bandit29@bandit:/tmp/sandias$ ls
bandit29@bandit:/tmp/sandias$ git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit29/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit29/.ssh/known_hosts).
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit29-git@localhost's password:
Permission denied, please try again.
bandit29-git@localhost's password:
Permission denied, please try again.
bandit29-git@localhost's password:
remote: Enumerating objects: 16, done.
remote: Counting objects: 100% (16/16), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 16 (delta 2), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (16/16), 1.44 KiB | 1.44 MiB/s, done.
Resolving deltas: 100% (2/2), done.
bandit29@bandit:/tmp/sandias$ ls -la
total 320
drwxrwxr-x    3 bandit29 bandit29   4096 Sep 21 19:23 .
drwxrwx-wt 8718 root     root     315392 Sep 21 19:24 ..
drwxrwxr-x    3 bandit29 bandit29   4096 Sep 21 19:24 repo
bandit29@bandit:/tmp/sandias$ cd repo
bandit29@bandit:/tmp/sandias/repo$ ls -la
total 16
drwxrwxr-x 3 bandit29 bandit29 4096 Sep 21 19:24 .
drwxrwxr-x 3 bandit29 bandit29 4096 Sep 21 19:23 ..
drwxrwxr-x 8 bandit29 bandit29 4096 Sep 21 19:24 .git
-rw-rw-r-- 1 bandit29 bandit29  131 Sep 21 19:24 README.md
bandit29@bandit:/tmp/sandias/repo$ cat README.md
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>

bandit29@bandit:/tmp/sandias/repo$ git log
commit 1748acec99ba66676acd551c2932fb9fc14a98a3 (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Sep 1 06:30:26 2022 +0000

    fix username

commit c27fff763003bb1d57d311e6763211110b94cc87
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Sep 1 06:30:26 2022 +0000

    initial commit of README.md
bandit29@bandit:/tmp/sandias/repo$ git show 1748acec99ba66676acd551c2932fb9fc14a98a3
commit 1748acec99ba66676acd551c2932fb9fc14a98a3 (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Sep 1 06:30:26 2022 +0000

    fix username

diff --git a/README.md b/README.md
index 2da2f39..1af21d3 100644
--- a/README.md
+++ b/README.md
@@ -3,6 +3,6 @@ Some notes for bandit30 of bandit.

 ## credentials

-- username: bandit29
+- username: bandit30
 - password: <no passwords in production!>

bandit29@bandit:/tmp/sandias/repo$ git show c27fff763003bb1d57d311e6763211110b94cc87
commit c27fff763003bb1d57d311e6763211110b94cc87
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Sep 1 06:30:26 2022 +0000

    initial commit of README.md

diff --git a/README.md b/README.md
new file mode 100644
index 0000000..2da2f39
--- /dev/null
+++ b/README.md
@@ -0,0 +1,8 @@
+# Bandit Notes
+Some notes for bandit30 of bandit.
+
+## credentials
+
+- username: bandit29
+- password: <no passwords in production!>
+
bandit29@bandit:/tmp/sandias/repo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/master
  remotes/origin/sploits-dev
bandit29@bandit:/tmp/sandias/repo$ git checkout remotes/origin/dev
Note: switching to 'remotes/origin/dev'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 2b1395f add data needed for development
bandit29@bandit:/tmp/sandias/repo$ git log
commit 2b1395f00cfb986163082c50100be5be8f249f64 (HEAD, origin/dev)
Author: Morla Porla <morla@overthewire.org>
Date:   Thu Sep 1 06:30:26 2022 +0000

    add data needed for development

commit 989df8073e16b5f7ec337f51bc1f60bd2f6b7e0b
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Sep 1 06:30:26 2022 +0000

    add gif2ascii

commit 1748acec99ba66676acd551c2932fb9fc14a98a3 (origin/master, origin/HEAD, master)
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Sep 1 06:30:26 2022 +0000

    fix username

commit c27fff763003bb1d57d311e6763211110b94cc87
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Sep 1 06:30:26 2022 +0000

    initial commit of README.md
bandit29@bandit:/tmp/sandias/repo$ git show 2b1395f00cfb986163082c50100be5be8f249f64
commit 2b1395f00cfb986163082c50100be5be8f249f64 (HEAD, origin/dev)
Author: Morla Porla <morla@overthewire.org>
Date:   Thu Sep 1 06:30:26 2022 +0000

    add data needed for development

diff --git a/README.md b/README.md
index 1af21d3..a4b1cf1 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for bandit30 of bandit.
 ## credentials

 - username: bandit30
-- password: <no passwords in production!>
+- password: xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS

bandit29@bandit:/tmp/sandias/repo$

```

**Referencias** 
