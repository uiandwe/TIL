# -*- coding: utf-8 -*-
# !/bin/python3

import re

def firstNameEmailID(text):
    regex = re.compile(r'([a-z]+) ([a-z]+)@gmail.com')
    matchobj = regex.search(text)
    if matchobj != None:
        areaCode = matchobj.group(1)
        print(areaCode)


firstNameEmailID("riya riya@gmail.com")
firstNameEmailID("julia julia@julia.me")
