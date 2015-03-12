TableToAnki
===========
TableToAnki is a simple tool for converting two-dimensional tabular data into an Anki deck.

Just put your whitespace-separated table into an empty file, add the row and column headers for the table on separate lines
at the top, and run it through tabletoanki.py! It will output a CSV formatted file that you can import into Anki.

Usage
=====

```
usage: tabletoanki.py [-h] [-t] [-n] [-or | -oc] table_file

positional arguments:
  table_file            Filename of the table you want to convert into a deck.

optional arguments:
  -h, --help            show this help message and exit
  -t, --transpose       Transpose table so the row header values appear first
                        in the CSV instead of the column header values
  -n, --newlines        Add a new line between the row and column header text
                        on the front of the card
  -or, --order-cards-by-row
                        Orders the CSV by row index, then column index
  -oc, --order-cards-by-column
                        Orders the CSV by column index, then row index
```

Example
=======

Multiplication table
--------------------
example2.txt contains a multiplication table up to 3 x 3. In order to produce good looking Anki cards for this use case,
the first line is blank and the second line contains a multiplication symbol:

```

×
    1   2   3
1   1   2   3
2   2   4   6
3   3   6   9

```

Running this through TableToAnki gives the following output CSV:

```
1 × 1,"1"
2 × 1,"2"
3 × 1,"3"
1 × 2,"2"
2 × 2,"4"
3 × 2,"6"
1 × 3,"3"
2 × 3,"6"
3 × 3,"9"
```

Pretty nifty, huh?

Blackjack
---------
If you don't know Blackjack, don't worry! All you have to know is that it's a card game played against a casino,
where you have a hand of a certain value and the card dealer has a visible card on the table. Depending on the visible card
and your hand's value, you should typically use a certain move (doubling, hitting, or sticking).
By the way, this readme doesn't constitute advice, it's just an example file! Don't sue me!

The headers for example.txt look like:

```
Hard
Dealer shows
```

With no options passed to TableToAnki, this means the front of cards will be of the form

```
Hard <row value> Dealer shows <column value>,"Cell value"
```

If you wanted the 'Hard X' and 'Dealer shows Y' to appear on separate lines,
pass in the --newline (or -n) option. Then you'll get this:

```
Hard X <br>Dealer shows Y
```

which will give you what you want if you import it into Anki with HTML enabled.

Here's a bit of the example table:

```
Hard    2   3   4   5   6   7   8   9   10  A
5       H   H   H   H   H   H   H   H   H   H
6       H   H   H   H   H   H   H   H   H   H
7       H   H   H   H   H   H   H   H   H   H
8       H   H   H   H   H   H   H   H   H   H
9       H   Dh  Dh  Dh  Dh  H   H   H   H   H
```

TableToAnki is clever enough to strip off the 'Hard' in the top-left, taking only the actual table data.

Here's a bit of the output:

```
...
Hard 20 Dealer shows 8,"S"
Hard 21 Dealer shows 8,"S"
Hard 5 Dealer shows 9,"H"
Hard 6 Dealer shows 9,"H"
Hard 7 Dealer shows 9,"H"
...
```

Ordering
========
The CSV generated by TableToAnki orders the cards by column value and then row value by default. For example, in the Blackjack
table above we see the output:

```
Hard 5 Dealer shows 2,"H"
Hard 6 Dealer shows 2,"H"
Hard 7 Dealer shows 2,"H"
Hard 8 Dealer shows 2,"H"
Hard 9 Dealer shows 2,"H"
...
```

If we wanted to order by our hand's value instead of the dealer's visible card, we can pass in --order-by-row-header (or -or)
and get the following:

```
Hard 5 Dealer shows 2,"H"
Hard 5 Dealer shows 3,"H"
Hard 5 Dealer shows 4,"H"
Hard 5 Dealer shows 5,"H"
Hard 5 Dealer shows 6,"H"
...
```

Transposing
===========
If you want the column header to appear first on the card instead of the row header, pass in --transpose (or -t).
Using the blackjack example with only the -t argument yields:

```
Dealer shows 2 Hard 5,"H"
Dealer shows 2 Hard 6,"H"
Dealer shows 2 Hard 7,"H"
Dealer shows 2 Hard 8,"H"
Dealer shows 2 Hard 9,"H"
Dealer shows 2 Hard 10,"Dh"
Dealer shows 2 Hard 11,"Dh"
...
```

Missing values
==============
If you have an unknown value in your table, replace it with the string 'MISSING' and that cell won't output a line in the CSV.

Known issues
============
Header names can't contain commas, and neither can the row or column names.
