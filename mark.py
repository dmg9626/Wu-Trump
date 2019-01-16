#!/usr/bin/python

import markovify
import os
import sys
import collections

# reads each file in folder sequentially and returns contents
def ReadFolder(fname):
    txt = ""
    for filename in os.listdir(fname):
        path = fname + "/" + filename
        f = open(path)
        txt += f.read()
    return txt


wutang = ReadFolder("WuTang")
trump = ReadFolder("Trump")

text = wutang + trump

# Build the model
text_model = markovify.NewlineText(text)

# Print three randomly-generated sentences of no more than 140 characters
#for i in range(10):
#    print(text_model.make_short_sentence(140))

# Print five randomly-generated sentences
for i in range(10):
    print(text_model.make_sentence())
