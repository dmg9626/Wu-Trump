#!/usr/bin/python

import markovify
import os
import sys
import collections

# reads each file in folder sequentially and returns contents
def ReadFolder(fname):
    txt = ""
    for filename in os.listdir(fname):
        # create path to file
        path = fname + "/" + filename

        if os.path.isdir(path):
            txt += ReadFolder(path)
        else:
            # open and read file
            f = open(path)
            txt += f.read()
    return txt


# Read in Wu tang lyrics and trump tweets
wutang = ReadFolder("WuTang")
trump = ReadFolder("Trump")

# Put them together (todo: consider mixing them randomly - this might help build a better markov dictionary)
text = wutang + trump

# Build the model
text_model = markovify.NewlineText(text)

# Print three randomly-generated sentences of no more than 140 characters
#for i in range(10):
#    print(text_model.make_short_sentence(140))

# Print five randomly-generated sentences
for i in range(10):
    print(text_model.make_sentence())

    # todo: ask me if I like it
    #       save to file if i type 'y', or discard otherwise
