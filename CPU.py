from instructions_6502 import Instructions
from instructions_6502 import LDA
class CPU:
    def __init__(self):
        self.registers = []

    #Take in instruction as bytes
    def instr(self,instruction:Instructions):
        #Process instructions
        instruction.pick_instr()



