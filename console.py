#!/usr/bin/python3
"""module that contains entry point of the command interpreter"""

import cmd
import shlex
import models
import ast

from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """All the command of the aplication"""
    prompt = "(hbnb)"

    errors = {
        "missingClass": "** class name missing **",
        "wrongClass": "** class doesn't exist **",
        "missingID": "** instance id missing **",
        "wrongID": "** no instance found **",
        "missingAttr": "** attribute name missing **",
    }

    classes = [
        "BaseModel", "User", "Amenity", "City", "Place", "Review", "State"
    ]

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

    def do_create(self, arg):
        """
        Instance of BaseModel that saves it and prints the id.
        """
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            new = eval(args[0])()
            new.save()
            print(new.id)
        else:
            print(self.errors["wrongClass"])

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            if len(args) < 2:
                print(self.errors["missingID"])
            else:
                key = args[0] + '.' + args[1]
                if key in models.storage.all().keys():
                    print(models.storage.all()[key])
                else:
                    print(self.errors["wrongID"])
        else:
            print(self.errors["wrongClass"])

    def do_destroy(self, arg):
        """Delete an Instance"""
        args = shlex.split(arg)
        models.storage.reload()
        if len(arg) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            if len(args) < 2:
                print(self.errors["missingID"])
            else:
                key = args[0] + '.' + args[1]
                if key in models.storage.all().keys():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print(self.errors["wrongID"])
        else:
            print(self.errors["wrongClass"])

    def all(self, arg):
        """print all string representation of all instances"""
        args = shlex.split(arg)
        models.storage.reload()
        arch = models.storage.all().values()
        if len(args) < 1:
            print([v.__str__() for v in arch])
        elif args[0] in self.classes:
            print([v.__str__() for v in arch if type(v) is eval(args[0])])
        else:
            print(self.errors["wrongClass"])

    def do_update(self, arg):
        """Updates an instance based on the class name"""
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            if len(args) < 2:
                print(self.errors["missingID"])
            else:
                key = args[0] + '.' + args[1]
                if key in models.storage.all().keys():
                    if len(args) < 3:
                        print(self.errors["missingAttr"])
                    else:
                        obj = models.storage.all()[key]
                        try:
                            attr_type = type(getattr(obj, args[2]))
                            args[3] = attr_type(args[3])
                        except Exception:
                            try:
                                args[3] = int(args[3])
                            except Exception:
                                try:
                                    args[3] = float(args[3])
                                except Exception:
                                    pass

                        setattr(obj, args[2], args[3])
                        obj.save()
                else:
                    print(self.errors["wrongID"])
        else:
            print(self.errors["wrongClass"])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
