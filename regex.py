# -*- coding: utf-8 -*-

import re
import codecs


def open_file(filename):
    raw_messages = []
    arq = codecs.open(filename, "r", "utf-8-sig")
    content = arq.read()
    arq.close()
    lines = content.split("\n")
    lines = [l for l in lines if len(l) != 1]
    for l in lines:
        raw_messages.append(l.encode("utf-8"))
    return raw_messages



p = re.compile(
    ur'(?P<datetime>(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{1,2}\,\s{0,1}((1[0-2]|0?[1-9]):([0-5][0-9]) ([AaPp][Mm])))\s{0,1}\-\s{0,1}')
test_str = u"29/03/14 15:48:05: John Smith changed the subject to â€œTestâ€\n\n29/03/14 16:10:39: John Smith joined\n\n29/03/14 16:10:40: Person:2 joined\n\n29/03/14 16:10:40: John Smith: Hello!\n\n29/03/14 16:11:40: Person:2: some random words,\n\n29/03/14 16:12:40: Person3 joined\n\n29/03/14 16:13:40: John: Smith: Hello!Test message with newline\nAnother line of the same message\nAnother line.\n\n29/03/14 16:14:43: Person:2: Test message using as last word joined\n\n29/03/14 16:15:57: Person3 left\n\n29/03/14 16:17:16: Person3 joined\n\n29/03/14 16:18:21: Person:2 changed the group icon\n\n29/03/14 16:19:16: Person3 was removed \n\nMar 16, 7:23 PM - ‪Person:2: Test message using as last word left\n"

re.findall(p, test_str)

test_str = u"29/03/14 15:48:05: John Smith changed the subject to â€œTestâ€\n\n29/03/14 16:10:39: John Smith joined\n\n29/03/14 16:10:40: Person:2 joined\n\n29/03/14 16:10:40: John Smith: Hello!\n\n29/03/14 16:11:40: Person:2: some random words,\n\n29/03/14 16:12:40: Person3 joined\n\n29/03/14 16:13:40: John: Smith: Hello!Test message with newline\nAnother line of the same message\nAnother line.\n\n29/03/14 16:14:43: Person:2: Test message using as last word joined\n\n29/03/14 16:15:57: Person3 left\n\n29/03/14 16:17:16: Person3 joined\n\n29/03/14 16:18:21: Person:2 changed the group icon\n\n29/03/14 16:19:16: Person3 was removed \n\n29/03/14 16:20:43: Person:2: Test message using as last word left"

a = re.findall(reg_string, test_str)
print a
datata = []
test_list = open_file("data.txt")
print test_list
print test_list[0:10]
print type(test_list)
test_string = "\n".join(test_list)
print test_string

a = re.findall(reg_string, test_string)
print a
