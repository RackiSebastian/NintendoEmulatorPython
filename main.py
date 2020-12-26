import argparse


def main():
    parser = argparse.ArgumentParser(description="Nintendo Simulator")
    parser.add_argument('rom_path',
                        metavar='R',
                        type=str,
                        help='path to nintento rom')

    args = parser.parse_args()

    print(args.rom_path)

    '''Reading in ASCII values '''
    with open(args.rom_path,'rb') as SMB_file:
        print(SMB_file.readlines())

    pass


if __name__ == '__main__':
    main()
