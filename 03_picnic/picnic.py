#!/usr/bin/env python3
"""
Author : sazli <sazli@localhost>
Date   : 2022-10-20
Purpose: Picnic Game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs = '+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    parser.add_argument('-n',
                        '--nocoma',
                        help='Print with no coma delimiter',
                        action='store_true')

    parser.add_argument('-d',
                        '--delimiter',
                        help='Delimiter to be used beside coma',
                        metavar='str',
                        type=str
                        )


    return parser.parse_args()


# --------------------------------------------------
def produce_msg_nocoma(items, sorted):
    """ Taking the items and then returning the complete message """
    if sorted:
        items.sort()
    
    items[-1] = 'and ' + items[-1]
    return f"You are bringing {' '.join(items)}."


# --------------------------------------------------
def produce_msg(items, sorted):
    """ Taking the items and then returning the complete message """
    item_total = len(items)
    if sorted:
        items.sort()
    
    if item_total == 1:
        return f'You are bringing {items[0]}.'
    else:
        items[-1] = 'and ' + items[-1]
        if item_total == 2:
            return f"You are bringing {' '.join(items)}."
        else:
            return f"You are bringing {', '.join(items)}."


def validate_delimiter(delimiter, nocoma):
    """ Validate the condition and content of delimiter """
    if delimiter == None:
        return 'NO DELIMITER'
    else:
        if nocoma:
            return 'ERROR'
        if delimiter == ',':
            return 'NO DELIMITER'
        if len(delimiter) > 1:
            return 'ERROR'

        return 'DELIMITER'


def produce_msg_delimiter(items, sorted, delimiter):
    """ Producing message with requested delimiter """
    if sorted:
        items.sort()
    
    return f"You are bringing {delimiter.join(items)}."

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    delimiter = validate_delimiter(args.delimiter, args.nocoma)
    if delimiter == 'ERROR':
        print('Error : Delimiter should be char and can not be used together with nocoma')
        return
    elif delimiter == 'NO DELIMITER':
        if args.nocoma and len(args.item) > 2:
            print(produce_msg_nocoma(args.item, args.sorted))
        else:
            print(produce_msg(args.item, args.sorted))
    else:
        print(produce_msg_delimiter(args.item, args.sorted, args.delimiter))

# --------------------------------------------------
if __name__ == '__main__':
    main()
