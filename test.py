# -*- coding: utf-8 -*-


import codecs
import re


def open_file(filename):
    '''

    :param filename: filename of the input file
    :return: the whole file as a single unicode string and newlines separated by /n
    '''
    raw_messages = []
    arq = codecs.open(filename, "r", "utf-8-sig")
    content = arq.read()
    arq.close()
    lines = content.split("\n")
    lines = [l for l in lines if len(l) != 1]
    for l in lines:
        raw_messages.append(l.encode("utf-8"))
    raw_messages = "\n".join(raw_messages)
    return raw_messages


p = re.compile(ur'(?P<phonenum>\+\(?\d{2,4}\)?[\d\s-]{3,})')
test_str = open_file('data.txt')

a = re.findall(p, test_str)
print a