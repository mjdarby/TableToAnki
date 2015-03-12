#!/usr/bin/python

# This file is part of TableToAnki
# Released under the MIT License
# Copyright 2015 Matthew Darby

import sys, argparse
from collections import OrderedDict

def print_inner_loop():
    """Because everything is, er, global, this function doesn't
    need any arguments."""
    if row_map[key][i] != "MISSING":
        if not args.transpose:
            print(header_texts[0] + " ",
                  key + " ",
                  br_text,
                  header_texts[1] + " ",
                  x,
                  ",",
                  "\"" + row_map[key][i] + "\"",
                  sep='')
        else:
            print(header_texts[1] + " ",
                  x + " ",
                  br_text,
                  header_texts[0] + " ",
                  key,
                  ",",
                  "\"" + row_map[key][i] + "\"",
                  sep='')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description= "Converts tabular data \
    into Anki-importable CSV files. Remember to enable HTML imports in Anki to \
    make sure everything works smoothly! Also remember you include your row and \
    column header text in your table files. See example.txt for an example!")
    parser.add_argument("table_file", help="Filename of the table you want to \
    convert into a deck.")
    parser.add_argument("-t", "--transpose", action="store_true",
                        help="Transpose table so the row header values appear \
                        first in the CSV instead of the column header values")
    parser.add_argument("-n", "--newlines", action="store_true",
                        help="Add a new line between the row and column header\
                        text on the front of the card")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-or", "--order-cards-by-row", action="store_true",
                       help="Orders the CSV by row index, then column index")
    group.add_argument("-oc", "--order-cards-by-column", action="store_true",
                       help="Orders the CSV by column index, then row index")
    args = parser.parse_args()

    try:
        table_file = open(args.table_file)
        table_text = table_file.read()
        table_file.close()
    except IOError:
        print("Could not read file {}".format(sys.argv[1]))
        sys.exit(1)

    header_texts = table_text.splitlines()[0:2]
    # Produce a list of lists that we can easily index into
    table_list = [x.split() for x in table_text.splitlines()[2:]]
    header = table_list[0]
    rows = table_list[1:]

    # Cut out the top-left element if present
    if len(header) == len(rows[0]):
        header = table_list[0][1:]

    row_map = OrderedDict()
    for row in rows:
        row_map[row[0]] = row[1:]

    br_text = "<br>" if args.newlines else ""
    if not args.order_cards_by_row: # Yes, the oc option is a ruse
        for i, x in enumerate(header):
            for key in row_map:
                print_inner_loop()

    if args.order_cards_by_row:
        for key in row_map:
            for i, x in enumerate(header):
                print_inner_loop()
