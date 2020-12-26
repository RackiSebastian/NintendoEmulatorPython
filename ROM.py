KBS = 16384


class ROM():
    def __init__(self, byts: bytes):
        '''
            Instructions start at 16kb
            Represent each byte of data
            8 bits in each byte of data
            16384 = 16kb
            '''
        self.HEADER = 16
        self.prg_block = 2
        self.byts = byts
        self.instructions = byts[self.HEADER:16 + KBS * self.prg_block]

    def get_instr(self, position):
        # Returns an int (should be a byte will update later)
        return self.byts[position:position + 1]
