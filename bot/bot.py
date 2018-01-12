#!/usr/bin/python3
import os
import aiml


class Bot(object):

    def __init__(self):
        self.k = aiml.Kernel()
        self.BRAIN_FILE="bot/brain.dump"
        # To increase the startup speed of the bot it is
        # possible to save the parsed aiml files as a
        # dump. This code checks if a dump exists and
        # otherwise loads the aiml from the xml files
        # and saves the brain dump.
        if os.path.exists(self.BRAIN_FILE):
            print("Loading from brain file: " + self.BRAIN_FILE)
            self.k.loadBrain(self.BRAIN_FILE)
        else:
            print("Parsing aiml files")
            self.k.bootstrap(learnFiles="bot/std-startup.aiml", commands="load aiml b")
            print("Saving brain file: " + self.BRAIN_FILE)
            self.k.saveBrain(self.BRAIN_FILE)

    # Endless loop which passes the input to the bot and prints
    # its response
    def get_response(self, query):
        return self.k.respond(query)
