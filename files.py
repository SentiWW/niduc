def read_file(file_name):
    """
    Function reads data from file and return it as list of bits
    :param file_name: Name of file
    :return: File content as list of bits
    """

    with open(file_name, mode="rb") as file:
        file_content = "".join("{:08b}".format(x) for x in file.read())  # reading content from file
        # the data is complemented with 0 to 8 bits

        file.close()
    return [int(x) for x in file_content]       # transforming string to list of bits


def write_file(file_name, bits):
    """
    Function write bits to file
    :param file_name: Name of file
    :param bits: Bits to write
    """

    ascii_codes = []
    for i in range(0, len(bits), 8):
        ascii_codes.append(int("".join(str(x) for x in bits[i:i + 8]), 2))    # converting bits to ASCII codes

    to_write = bytearray(ascii_codes)           # converting characters ASCII codes into writable form

    with open(file_name, mode="wb") as file:
        file.write(to_write)                    # writing to file
        file.close()
