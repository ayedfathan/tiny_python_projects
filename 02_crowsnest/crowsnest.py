#!/usr/bin/env python3
"""
Author : sazli <sazli@localhost>
Date   : 2022-10-16
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A Word')

    return parser.parse_args()


def produce_ahoy(word):
    """ Return message complied with the word pass as the argument """

    article = 'an' if word.strip().lower()[0] in 'aiueo' else 'a'
    return f'Ahoy, Captain, {article} {word.strip()} off the larboard bow!'

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    print(produce_ahoy(word))

# --------------------------------------------------
if __name__ == '__main__':
    main()
