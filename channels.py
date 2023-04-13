from enum import Enum

import numpy as np


class States(Enum):
    """
    Enum represent states of channel

    Elements
    --------
    GOOD:
        State where bit is sent correctly
    BAD:
        State where bit is sent incorrectly
    """
    GOOD = 0
    BAD = 1


class GilbertModel:
    """
    Telecommunication channel that simulates Gilbert model (Simple channel with memory)
    For consistency channel is implemented like channels from komm library

    Channel starts in state GOOD
    For every sent bit channel may change state to BAD with probability _p_g2b
        or stay in state GOOD with probability 1 - _p_g2b

    After transition to state BAD:
    For every sent bit channel may change state to GOOD with probability _p_b2g
        or stay in state BAD with probability 1 - _p_b2g

    The result of sending bit is:
        - same as input if channel is in state GOOD
        - negated input if channel is in state BAD

    Attributes
    ----------
    _state :type States
        State of channel that implements channel memory
    _p_g2b:
        Probability of changing state from GOOD to BAD
    _p_b2g
        Probability of changing state from BAD to GOOD

    Methods
    -------
    __call__:
    Method simulates sending message through channel modeled by Gilbert model
    Method is compatible with encoders and decoders from komm library
    """

    def __init__(self, good_to_bad_transition_probability, bad_to_good_transition_probability):
        self._state = States.GOOD
        self._p_g2b = good_to_bad_transition_probability
        self._p_b2g = bad_to_good_transition_probability

    def __call__(self, message: list):
        """
        Method simulates sending message through channel modeled by Gilbert model
        Method is compatible with encoders and decoders from komm library
        :param message:
        :return: Message after sending through channel
        """

        output = []                                     # list for output bits
        for bit in message:
            if self._state == States.GOOD:              # if state is GOOD
                if np.random.rand() < self._p_g2b:
                    self._state = States.BAD            # state change
                    output.append((bit + 1) % 2)        # trick for bit negation without if
                else:
                    output.append(bit)                  # bit passed channel without negation
            else:                                       # if state is BAD
                if np.random.rand() < self._p_b2g:
                    self._state = States.GOOD           # state change
                    output.append(bit)                  # bit passed channel without negation
                else:
                    output.append((bit + 1) % 2)        # trick for bit negation without if

        return output
