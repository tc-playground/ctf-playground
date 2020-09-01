# Research Questions

## Hide data in an image?

1. Steganography - [Oxrick](https://0xrick.github.io/lists/stego/)

    1. `sudo apt instal -y steghide`

        2. `steghide info file` - Displays info about a file whether it has embedded data or not.

        3. `steghide extract -sf file` : Extracts embedded data from a file.

---

## Task 2 - Research Questions

1. In the Burp Suite Program that ships with Kali Linux, what mode would you use to manually send a request (often repeating a captured request numerous times)?

    * [Burp Repeater](https://portswigger.net/burp/documentation/desktop/tools/repeater/using)

2. What hash format are modern Windows login passwords stored in?

    * [NTLM in the SAM file](https://resources.infosecinstitute.com/category/certifications-training/ethical-hacking/breaking-password-security/breaking-windows-passwords/)

3. What are automated tasks called in Linux?

    - `CRON jobs`

4. What number base could you use as a shorthand for base 2 (binary)?

    * [Base 8/16](http://byte-notes.com/number-bases/)

5. If a password hash starts with $6$, what format is it (Unix variant)?

    * `MD5` hashes begin with `$1$`.

    * `SHA-512` hashes begin with `$6$`.

    ```
    $1$ md5
    $2a$ Blowfish
    $2y$ Blowfish, with correct handling of 8 bit characters
    $5$ sha256
    $6$ sha512
    ```

    * [/etc/shadow hash formats](https://www.aychedee.com/2012/03/14/etc_shadow-password-hash-formats/)

    * [How valuable is secrecy of an algorithm? (](https://security.stackexchange.com/questions/55991/why-does-md5-hash-starts-from-1-and-sha-512-from-6-isnt-it-weakness-in-its)

    * The UNIX variant is: `sha512crypt` - [Hashcat](https://hashcat.net/forum/thread-1405.html)

        * [Crypt - Wikipedia](<https://en.wikipedia.org/wiki/Crypt_(C)>)

---

## Task 3 - Vulnerability Research

*   __Exploitation Research Resources__

    1. [Exploit Database](https://www.exploit-db.com/)

        1. `searchsploit` - Command line tool.

    2. [National Vulnerability Database](https://nvd.nist.gov/vuln/search)

    3. [Common Vulnerabilities and Exposures](https://cve.mitre.org/)

1. What is the CVE for the 2020 Cross-Site Scripting (XSS) vulnerability found in WPForms?

    * `CVE-2020-10385`

2. There was a Local Privilege Escalation vulnerability found in the Debian version of Apache Tomcat, back in 2016. What's the CVE for this vulnerability?

    * `CVE-2016-1240`

3. What is the very first CVE found in the VLC media player?

    * `CVE-2007-0017`

4. If I wanted to exploit a 2020 buffer overflow in the sudo program, which CVE would I use?

    * `CVE-2019-18634`

---

## Task 4 - Manual Page Research

-   **Manual Pages** - The `man` command can be used to find more information on a Linux `command` and its `options`.

1. `SCP` is a tool used to copy files from one computer to another. What switch would you use to copy an entire directory?

    * `-r`

2. `fdisk` is a command used to view and alter the partitioning scheme used on your hard drive. What switch would you use to list the current partitions?

    * `-l`

3. `nano` is an easy-to-use text editor for Linux. There are arguably better editors (Vim, being the obvious choice); however, nano is a great one to start with. What switch would you use to make a backup when opening a file with nano?

    * `-B`

4. `Netcat` is a basic tool used to manually send and receive network requests. What command would you use to start netcat in listen mode, using port 12345?

    * `nc -l -p 12345`

---

## References

-   [Learn Linux Room](https://tryhackme.com/room/zthlinux)

-   [Google Dorking Room](https://tryhackme.com/room/googledorking)
