#!/usr/bin/env python3

import sys

# YOUR CODE HERE

# We open STDIN and STDOUT
#with sys.stdin as fin:
#    with sys.stdout as fout:
        # For every line in STDIN
#        for line in fin:
            # Strip off leading and trailing whitespace
#            line = line.strip()
            # We split the line into word tokens. Use whitespace to split.
            # Note we don't deal with punctuation.
#            words = line.split()
            # Now loop through all words in the line and output
#            for word in words:
#                fout.write("{0}{1}1\n".format(word, sep))


# Reads data from STDIN,
with sys.stdin as fin:
    # Skips the first line (The first line of 2001.csv is the header that has the column titles.)
    next(fin)
    with sys.stdout as fout:
        # For every line in STDIN
        for line in fin:
            # Strip off leading and trailing whitespace
            line = line.strip()
            # We split the line into word tokens. Use whitespace to split.
            # Note we don't deal with punctuation.
            words = line.split(',')
            # Outputs to STDOUT the Origin and AirTime columns separated with a tab.
            fout.write("{0}\t{1}\n".format(words[16], words[13]))