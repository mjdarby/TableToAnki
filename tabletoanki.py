#!/usr/bin/python

import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: tabletoanki.py <table.txt>")
        sys.exit(2)

    try:
        table_file = open(sys.argv[1])
        table_text = table_file.read()
        table_file.close()
    except IOError:
        print("Could not read file {}".format(sys.argv[1]))
        sys.exit(1)

    # Produce a list of lists that we can easily index into
    table_list = [x.split() for x in table_text.splitlines()]
    header = table_list[0][1:]
    rows = table_list[1:]
    row_map = {row[0]: row[1:] for row in rows}

    for i, x in enumerate(header):
        for key in row_map:
            print("Pair", key, "Dealer shows", x, ",", row_map[key][i])
