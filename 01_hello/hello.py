#!/usr/bin/python3
"""
Author : Said Azli said.azli@gmail.com
Purpose : Saying hello with paramete
"""


import argparse


def get_args():
    """ Getting name argumenent from shell """
    parser = argparse.ArgumentParser(description='Say Hello')
    parser.add_argument('-n',
                        '--name',
                        default='World',
                        help='Name to greet')
    return parser.parse_args()


def main():
    """ The main program body """
    args = get_args()
    print(f'Hello, {args.name}!')


if __name__ == '__main__':
    main()
