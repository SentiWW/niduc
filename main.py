file = open("test-data.txt")

for line in file:
    for char in line.strip():
        char_bytes = bytes(char, "utf-8")
        print(char_bytes.hex())