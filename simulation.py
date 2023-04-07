from copy import deepcopy

import komm


class Simulation:
    """
    Attributes
    ----------
    code :type komm.BlockCode
        Code to be used for message encoding and decoding in send method
    channel: callable object
        Channel model used to simulate sending messages

    Methods
    -------
    send:
        Method simulates sending message coded by self._code through self._channel
    """

    def __init__(self, code: komm.BlockCode, channel):

        # coder
        self.code = code

        # channel
        self.channel = channel

    def send(self, message):
        """
        Method simulates sending message coded by self._code through self._channel
        :param message: message to be sent
        :returns: sent message, number of errors and bit error rate
        """
        dim = self.code.dimension                               # code dimension - block length

        msg = deepcopy(message)                                 # message deep copy

        comp = (dim - len(msg) % dim) % dim                     # If message is shorter then multiple of block's length
        msg.extend(0 for _ in range(comp))                      # it is complemented with 0

        coded = []
        for i in range(0, len(msg), dim):
            coded.append(self.code.encode(msg[i:i + dim]))      # block encoding of message

        sent = [self.channel(x) for x in coded]                 # "sending" blocks through channel

        decoded = []
        for x in sent:
            decoded.extend(self.code.decode(x))                 # decoding blocks and merging output message

        out_msg = list(int(x) for x in decoded)[:len(decoded) - comp]   # unifying types and removing complementing

        num_of_errors = sum(1 for i in range(len(message)) if message[i] != out_msg[i])     # counting number of errors

        ber = num_of_errors / len(message)                      # counting bit error rate

        return out_msg, num_of_errors, ber
