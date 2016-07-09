#!/usr/bin/env python2

# -*- coding: utf-8 -*-


import codecs
import whatsapp


class Chat():

    def __init__(self, filename):
        self.filename     = filename
        self.raw_messages = []
        self.messages     = []     # List of Messages objects
        # self.features     = ChatFeatures() # Chat Features object
        self.senders      = []
        self.root         = ''


    def open_file(self):
        arq = codecs.open(self.filename, "r", "utf-8-sig")
        content = arq.read()
        arq.close()
        lines = content.split("\n")
        lines = [l for l in lines if len(l) != 1]
        for l in lines:
            self.raw_messages.append(l.encode("utf-8"))

    def parse_message(self):
        p = whatsapp.ParserWhatsapp(self.raw_messages)
        self.senders, self.messages = p.parse()





