import argparse
from CPU import CPU
from ROM import ROM
from instructions_6502 import Instructions, LDA


def main():
    parser = argparse.ArgumentParser(description="Nintendo Simulator")
    parser.add_argument('rom_path')

    args = parser.parse_args()

    '''Reading in Hex values '''
    with open(args.rom_path, 'rb') as SMB_file:
        l = SMB_file.read()

    rom = ROM(list(l))
    cpu = CPU()
    cpu.load_rom(rom)




if __name__ == '__main__':
    main()
