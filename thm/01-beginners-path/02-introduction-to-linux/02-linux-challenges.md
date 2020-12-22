# Linux Challenges

* [Room - Learn Challenges](https://tryhackme.com/room/linuxctf)

---

## The Basics 

* Flag 3

    * `cat /home/bob/.bash_history`

    * `history`

* Flag 4

    * `crontab -l`

    * `ls ls /var/spool/cron/crontabs`

* Find Flag 5

    * `find / -name flag5.txt 2>>/dev/null`

* Flag 6

    * `find / -name flag6.txt 2>>/dev/null`

    * `cat /home/flag6.txt | grep c9`

* Flag 7

    * `ps aux | grep flag`

* Flag 8

    * `find / -name flag8.* 2>>/dev/null`

    * `tar -xvf /home/bob/flag8.tar.gz`

* Flag 9

    * `cat /etc/hosts`

* Flag 10

    * `cat /etc/passwd`

---

## Linux Functionality

* Flag 11

    * `find / -name .bashrc -print 2>>/dev/null`

* Flag 12

    * `find / -name *motd* 2>>/dev/null`

    * `man motd`

    * `cat /etc/motd`

    * `cat /etc/update-motd.d/00-header`

* Flag 13

    * `diff script1 script2`

* Flag 14

    * `cat /var/log/flagtourteen.txt`

* Flag 15

    * `cat /etc/lsb-release`

* Flag 16

    * `cd l/a/g/1/6/is/cab4b7cae33c87794d82efa1e7f834e6/`

* Flag 18

    * `ls -lA`

* Flag 19

    * `sed -n 2345,2345p flag19`

    * or use `vim` -> `set number` -> `:2345`

---

## Data Representation, Strings and Permissions

* Flag 20

    * `cat flag20 | base64 -d; echo`

* Flag 21

    * `find / -name flag21.php 2>>/dev/null | xargs cat` -> `<?='MoreToThisFileThanYouThink';?>`
    * `file /home/bob/flag21.php`
    * `hexdump -C /home/bob/flag21.php`
    * `hd /home/bob/flag21.php`
    * `xxd /home/bob/flag21.php`



* Flag 22

    * Convert hex to ASCII
    * `xxd -r -p /home/alice/flag22; echo`

* Flag 23

    * `find / -name flag23 2>/dev/null | xargs cat | rev`

* Flag 24

    * `find / -name flag24 2>/dev/null`

    * `find / -name flag24 2>/dev/null | xargs strings | grep flag`

* Flag 26

    * `find / -xdev -type f -print0 2>/dev/null | xargs -0 grep -E '^4bceb[a-z0–9]{27}$' 2>/dev/null`

        * `find` opts

            * `-xdev` - Don't descend directories on other filesystems.

            * `-type` - Find files of a specific type {`f: regular`, `s: Socket`, etc.}

            * `print` - Print output to a file.
        
        * `xarg` opts

            * `-0` - Input items are terminated by a null character instead of by whitespace, and the quotes and backslash are not special.
        
        * `grep` opts

            * `-E` - For extended regular expressions.

* Flag 27

    * `su alice`
    * `sudo -l`
    * `sudo cat /home/flag27`

* Flag 28

    * `uname -a`

* Flag 29

    * `cat flag29 | sed 's/\s//g' | tr -d '\n' | tr ',' ' ' | awk '{print $NF}'`

---

## SQL, FTP, Groups and RDP 

* Flag 30

    * `curl localhost`

* Flag 31

    * `mysql -u root -p`
    * `show databases;`

* Flag 32

    * `use database_2fb1cab13bf5f4d61de3555430c917f4;`
    * `show tables;`
    * `select * from flags'`

* Flag32

    * `ssh root@3.249.115.245`
    * `scp alice@10.10.28.171:flag32.mp3 .`
    * `exit`
    * `scp root@34.254.223.37:flag32.mp3 .`

* Flag33

    * `cat /home/bob/.profile`

* Flag34

    * `su bob`
    * `env | grep flag34`

* Flag35

    * `groups`
    * `cat /etc/group | grep flag35`

* Flag36

    * `getent group hacker`
    * `groups`
    * `su bob`
    * `find / -type f -name flag36 2>/dev/null | xargs cat`




---

## Bash Profiles

```bash
garry@ip-10-10-209-100:~$ cat .bashrc 
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

```