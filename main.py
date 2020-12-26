import argparse
from CPU import CPU
from instructions_6502 import *

def main():
    parser = argparse.ArgumentParser(description="Nintendo Simulator")
    parser.add_argument('rom_path')

    args = parser.parse_args()

    print(args.rom_path)

    '''Reading in Hex values '''
    with open(args.rom_path,'rb') as SMB_file:
        l = SMB_file.readlines()


    cpu = CPU()
    '''
    Instructions start at 16kb 
    Represent each byte of data 
    8 bits in each byte of data 
    16384 = 16kb
    '''
    prg_block = 2
    HEADER_SIZE = 16
    KBS = 16384
    instructions = l[HEADER_SIZE:16+KBS * prg_block]

    '''process each instruction and see what it does(bytes)'''
    for instruction in list(instructions):
        instr = Instructions(instruction)
        cpu.instr(instruction)

if __name__ == '__main__':
    main()

