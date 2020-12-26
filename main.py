import argparse
from CPU import CPU

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
    '''
    #Change this too hardcoded
    prg_block = 2
    instructions = l[0][16:16+16384 * prg_block]
    print(instructions)
    print(cpu.instr(l[0][0:3]))


if __name__ == '__main__':
    main()

