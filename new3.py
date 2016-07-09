#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import codecs
import re
import pandas as pd
import numpy as np


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


regex_string = ur'(?P<DateTime>(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{1,2}\,\s{0,1}((1[0-2]|0?[1-9]):([0-5][0-9]) ([AaPp][Mm]))\s{0,1}\-\s{0,1})(?P<name>\+\(?\d{2,4}\)?[\d\s-]{3,}|\w+(?::\s*\w+)*|[\w\s]+?)(?:\s+(?P<action>joined|left|was removed|(?:created group \"\w+\")|changed the (?:subject to â€œ\w+â€|group icon))|\:\s(?P<message>(?:.+|\n(?!\n))+))'

data_format = re.compile(regex_string)

test_str = open_file('data.txt')

a = [m.groupdict() for m in data_format.finditer(
    test_str)]  # returns a LIST of tokenized elements tagged accordingly to their date-time, name-number, action = joined left, kicked and message
# as the list is tokenized according to the regex named capturing lists,
# reading it into pandas dataframe automatically parses the values accordingly to ther tags
# df['datetime','name','action','message']
df = pd.DataFrame(a)
# two new columns are added for sttoring the values of area searched and price searched into the dataframe
df['area'] = np.nan
df['price'] = np.nan
df['area'] = df['area'].astype(object)
df['price'] = df['price'].astype(object)

reg_area_string = ur'(?P<value>([0-9]*[.])?[0-9]+)\s*(sq[.]*|square)\s*(ft[.]*|m[tr*s*.]*|yd[.]*|feet|metre|yard[s]*|Yrd[s]*)*'
reg_area = re.compile(reg_area_string, re.IGNORECASE)

reg_price_string = ur'(?P<value>([0-9]*[.])?[0-9]+)\s*(cr[.]*|crore[s]*|l[.]*|lakh[s]*|lac[s]*|lack[s]*|th[.]*|thousand[s]*)\s*'
reg_price = re.compile(reg_price_string, re.IGNORECASE)

# searched into the 'message' column of each row and updated accordingly
for index, row in df.iterrows():
    area_str = [m.groupdict() for m in reg_area.finditer(row['message'])]
    price_str = [m.groupdict() for m in reg_price.finditer(row['message'])]
    # if values are found, then updated to the dataframe accordingly
    if area_str:
        df.set_value(index, 'area', area_str)
    if price_str:
        df.set_value(index, 'price', price_str)

# the Nan values by which the df was initialzed are changed to whitespace for csv
df1 = df.replace(np.nan, ' ', regex=True)
# the dataframe is outputted to CSV
df1.to_csv('output.csv')