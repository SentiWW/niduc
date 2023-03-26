with open("test-data.txt", mode='rb') as file:
    file_content = file.read()

for byte in file_content:
    print(byte)
