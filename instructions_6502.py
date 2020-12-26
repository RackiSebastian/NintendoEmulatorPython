'''
Three things
1. I want whatever is at that position
2. I want whatever is at memory position x
3. I want whatever is x amount away from position x

Depending on indexing there is different data that can be used
so for example
aaaaaa
aa
aaaaa
'''
from abc import ABC, abstractmethod, abstractproperty


# To make this an abstract class you must inherit from ABC?>

class Instructions(ABC):
    '''
    @param: b is the byte (processing as an int at the moment for clarity
    before i figure out how to move it to hex

    '''

    def __init__(self, b):
        self.b = b

    @property
    def instr_len(self):
        return 1

    '''
    Different instructions different methods
    
    '''

    @abstractmethod
    def pick_instr(self):
        print(self.__str__())


class LDA(Instructions):
    instr_len = 2

    def __str__(self):
        return "LDA, Identifier: {}".format(self.b)

    def pick_instr(self):
        super().pick_instr()


class SEI(Instructions):
    instr_len = 1

    def __str__(self):
        return "SEI, Identifier: {}".format(self.b)

    def pick_instr(self):
        super().pick_instr()


class CLD(Instructions):
    instr_len = 1

    def __str__(self):
        return "CLD, Identifier: {}".format(self.b)

    def pick_instr(self):
        super().pick_instr()
