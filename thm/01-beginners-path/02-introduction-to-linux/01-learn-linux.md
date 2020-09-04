# Learn Linux

* [Room - Learn Linux](https://tryhackme.com/room/zthlinux)

---

## SSH

* Linux: `ssh <user>@<host>`

* Windows `PuTTY - Click around a bit.`

---

## Commands

* man, ls, cat, touch, su.

`ls -la`

`cat -n bob.txt`

`su -s /bin/bash`

`echo hello > file` - Over-write.

`echo hello >> file` - Append

`echo hello >> file2 && cat file2`

`sleep 5 &`

`echo $USER`

`cat test | grep 1234`

`The ; operator works a lot like &&, however it does not require the first command to execute successfully.`

    dsfgsdsfg; ls

---

File

`chmod <permissions> <file>`

    Digit	Meaning
    0   Nuffin
    1	That file can be executed
    2	That file can be written to
    3	That file can be executed and written to
    4	That file can be read
    5	That file can be read and executed
    6	That file can be written to and read
    7	That file can be read, written to, and executed.

    `chmod 777 file` === `chmod a+rwx file`

    `UGE`

`chown shiba2:shiba2 file`

`rm file`

`mv file /tmp`

`cp <file> <destination>`

`cd <directory>`

`mkdir <directory name>`

`ln source destination` - It's important to be very careful with hard links, as depending on what you're doing it can be very easy to erase data from a file.

`ln -s source destination` - It has full 777 perms meaning that in theory you can execute the symlink, however since it is just a reference, in reality it has the same perms as the original file.

* __Find__

    * `find` - listing every file in the current directory

    * `find /`

    * `find dir -user` to list every file owned by a specific user

    * `find dir -group` to list every file owned by a specific group

    * `man find`

* __grep__

    * `grep <regex> <file>`

    * `grep <regex> <file> <file2>`

    * `grep hello test -n`

---

* sudo <command>

    * `whoami`

    * `sudo -u bob`

    * `sudo -u jen whoami`

    * `sudo -l`

* User and Groups

    * `sudo adduser username`
    
    * `sudo addgroup groupname`

    * `sudo usermod -a -G <groups seperated by commas> <user>`.

    * Must be route to add users and groups.

    * `id` - Get basic user info.

* `nano`

* basic shell scripting

* Useful files

    * /etc/passwd - Stores user information - Often used to see all the users on a system
    * /etc/shadow - Has all the passwords of these users
    * /tmp - Every file inside it gets deleted upon shutdown - used for temporary files
    * /etc/sudoers - Used to control the sudo permissions of every user on the system
    * /home - The directory where all your downloads, documents etc are. - The equivalent on Windows is C:\Users\<user>
    * /root - The root user's home directory - The equivilent on Windows is C:\Users\Administrator
    * /usr - Where all your software is installed 
    * /bin and /sbin - Used for system critical files - DO NOT DELETE
    * /var - The Linux miscellaneous directory, a myriad of processes store data in /var
    * $PATH - Stores all the binaries you're able to run - same as $PATH on Windows

* apt install package

* __Processes__

    * `ps -ef`

    * `kill <PID>`

---

* __CTF__

    1. `cat /etc/passwd` - List users.

    2. `sudo -l` - List sudo configuration and permissions for current user. 
    
    3. `find / -user <username> -type f 2>>/dev/null` - Check files for each user.
    
    4. `su <username>` - Become user.

    









