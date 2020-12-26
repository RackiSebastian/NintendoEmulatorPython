from instructions_6502 import Instructions
from instructions_6502 import LDA, SEI, CLD
from ROM import ROM


class CPU:
    def __init__(self):
        self.registers = []
        self.rom = None
        self.state = True
        # Program counter starts at 16 and has current execution point
        self.pc = None
        self.mapper = {
            # 169 = A9 so we do an LDA
            bytes.fromhex('A9'): LDA,
            bytes.fromhex('78'): SEI,
            bytes.fromhex('D8'): CLD

        }

    # Take in instruction as bytes
    def instr(self, instruction: Instructions):
        # Process instructions
        instruction.pick_instr()

    def load_rom(self, rom: ROM):
        self.rom = rom
        self.pc = self.rom.HEADER
        self.state = True
        while self.state:
            instr = self.rom.get_instr(self.pc)
            '''add this so if we cant find it it wont crash but return None'''
            instruction = self.mapper.get(instr, None)
            if instruction is None:
                raise Exception("Instruction invalid!")

            instr_cls = instruction(instr)
            instr_cls.pick_instr()

            self.pc += instruction.instr_len

            # Turn byte into instruction from translation table
