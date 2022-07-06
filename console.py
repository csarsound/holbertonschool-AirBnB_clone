#!/usr/bin/python3
"""Console Command processor module to control Airbnb Console
"""
import cmd
import json
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Console Command processor class to control Airbnb Console
    """

    prompt = '(hbnb) '

    def do_EOF(self, args):
        """ EOF command to exit the program """
        print()
        return True

    def do_quit(self, args):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        """empty line
        """
        pass

if __name__ == '__main__':
    hb = HBNBCommand
    HBNBCommand().cmdloop()
