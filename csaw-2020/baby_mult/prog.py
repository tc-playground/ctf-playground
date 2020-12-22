#!/usr/bin/python3

input = open("program.txt", "r")
data = input.read()
print(data)
print

parts = data.split(",")
bytes = []
hexes = []
chars = []
unichars = []
for part in parts:
    part = part.strip()
    bytes.append(int(part))
    hexes.append(hex(int(part)))
    chars.append(chr(int(part)))
    unichars.append(unichr(int(part)))

print(bytes)
print()
print(hexes)
print()
print(chars)
print()
print(unichars)

# newFileByteArray = bytearray(bytes)
# output = open("out.bin", "wb")
# output.write(newFileByteArray)

# hex_out = open("hex_out.txt", "w")
# hex_str = ", ".join(hexes)
# hex_out.write(hex_str)
