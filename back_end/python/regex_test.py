# -*- coding: utf-8 -*-
import re

def phone_regex_format_replace(text):
    phonePattern = re.compile(r'^(\d{3})[-]?(\d{3})[-]?(\d{4})$')
    try:
        word1, word2, word3 = phonePattern.search(text).groups()
        return "{0}-{1}-{2}".format(word1, word2, word3)
    except Exception as e:
        print(e)
        return text


if __name__ == '__main__':
    text_mod = phone_regex_format_replace('8005551234')
    print(text_mod)
