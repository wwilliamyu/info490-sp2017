#!/usr/bin/env python3

import sys

# YOUR CODE HERE

# We open STDIN and STDOUT
# with sys.stdin as fin:
#    with sys.stdout as fout:
        # Keep track of current word and count
#        cword = None
#        ccount = 0
#        word = None   
        # For every line in STDIN
#        for line in fin:
            # We split the line into a word and count, based on predefined
            # separator token.
            #
            # Note we haven't dealt with punctuation.          
#            word, scount = line.split('\t', 1)            
            # We will assume count is always an integer value            
#            count = int(scount)
            # word is either repeated or new           
#            if cword == word:
#                ccount += count
#            else:
                # We have to handle first word explicitly
#                if cword != None:
#                    fout.write("{0:s}{1:s}{2:d}\n".format(cword, sep, ccount))            
                # New word, so reset variables
#                cword = word
#                ccount = count
#        else:
            # Output final word count
#            if cword == word:
#                fout.write("{0:s}{1:s}{2:d}\n".format(word, sep, ccount))
                
                

# Reads key-value pairs from STDIN,
with sys.stdin as fin:
    with sys.stdout as fout:
        # Computes the minimum and maximum air time for flights, with respect to each origin airport,
        origin = None
        c_origin = None
        c_min = None
        c_max = None
        # For every line in STDIN
        for line in fin:
            # We split the line into a word and count, based on predefined
            # separator token.
            #
            # Note we haven't dealt with punctuation.
            origin = line.split('\t')[0]
            airtime = line.split('\t')[1]
            
            # there are NA\n in there...
            if airtime != "NA\n":
                # we will assume airtime is always an integer value
                airtime = int(airtime)
                if c_origin == None:
                    # new
                    c_origin = origin
                    c_min = airtime
                    c_max = airtime
                elif origin == c_origin:
                    # repeated
                    c_min = min(c_min, airtime)
                    c_max = max(c_max, airtime)
                else:
                    # next
                    # Outputs to STDOUT the airports and the minimum and maximum air time for flights at each airport, separated with tabs.
                    fout.write("{0}\t{1}\t{2}\n".format(c_origin, c_min, c_max))
                    c_origin = origin
                    c_min = airtime
                    c_max = airtime
        else:
            # Output final word count
            if c_origin == origin:
                fout.write("{0}\t{1}\t{2}\n".format(c_origin, c_min, c_max))