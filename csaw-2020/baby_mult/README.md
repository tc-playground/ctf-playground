# baby_mult

* [baby_mult](https://ctf.csaw.io/challenges#baby_mult)

---

## Analyse Bytes

```bash
./prog.py
chmod +x out.bin
hexdump -C ./out.bin
file ./out.bin
objdump -D out.bin
```

```bash
# ./prog.py
objcopy -I binary -O elf64-x86-64 --binary-architecture i386 out.bin out.elf
chmod +x out.elf
file ./out.elf
objdump -D out.elf
```
