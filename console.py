#!/usr/bin/python3
"""module that contains entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """All the command of the aplication"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """
        Exit the program.
            usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        Exits the program.
            usage: EOF (ctrl+D)
        """
        return True

    def emptyline(self):
        """handles the emptyline"""
        pass


if __name__=="__main__":
    HBNBCommand().cmdloop()
