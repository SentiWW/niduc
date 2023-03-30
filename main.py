import komm


file = open("test-data.txt")

for line in file:
    for char in line.strip():
        char_bytes = bytes(char, "utf-8")
        print(char_bytes.hex())


# code length
n = 3

# channel crossover probability
p = 0.1

# message
msg = [1]

# coder
code = komm.RepetitionCode(n)

# channel
bsc = komm.BinarySymmetricChannel(p)


coded = code.encode(msg)                # coding message
y = bsc(coded)                          # "sending" message
decoded = code.decode(y)                # decoding message

print(decoded)
