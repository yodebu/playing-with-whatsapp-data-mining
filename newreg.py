#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import re


def open_file(filename):
		x = open(filename,'r')
		lines = x.readlines()
		mystr = '\t'.join([line.strip() for line in lines])
		return mystr


p = re.compile(ur'(?P<datetime>\d{2}\/\d{2}\/\d{2} \d{2}:\d{2}:\d{2}): (?P<name>\w+(?::\s*\w+)*|[\w\s]+?)(?:\s+(?P<action>joined|left|was removed|changed the (?:subject to â€œ\w+â€|group icon))|:\s(?P<message>(?:.+|\n(?!\n))+))')
test_str = u"29/03/14 15:48:05: John Smith changed the subject to â€œTestâ€\n\n29/03/14 16:10:39: John Smith joined\n\n29/03/14 16:10:40: Person:2 joined\n\n29/03/14 16:10:40: John Smith: Hello!\n\n29/03/14 16:11:40: Person:2: some random words,\n\n29/03/14 16:12:40: Person3 joined\n\n29/03/14 16:13:40: John: Smith: Hello!Test message with newline\nAnother line of the same message\nAnother line.\n\n29/03/14 16:14:43: Person:2: Test message using as last word joined\n\n29/03/14 16:15:57: Person3 left\n\n29/03/14 16:17:16: Person3 joined\n\n29/03/14 16:18:21: Person:2 changed the group icon\n\n29/03/14 16:19:16: Person3 was removed \n\n29/03/14 16:20:43: Person:2: Test message using as last word left"
 
result = re.findall(p, test_str)
print result

		
test_str = open_file('data.txt')
print test_str
print type(test_str)
result = re.findall(p, test_str)
print result
