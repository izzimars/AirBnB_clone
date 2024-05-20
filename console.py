#!/bin/python3
"""
base_geometry Module
====================

This module defines the MyList class, which inherits from
the built-in list class.

BaseGeometry:
    MyList: A subclass of list with additional functionality.

Public Function:
    None.

"""


import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    BaseGeometry Class

    A base class hat defines all common attributes/methods for
    other model.

    Public Methods:
        save: updates the public instance attribute updated_at with
              the current datetime
        to_dict: returns a dictionary containing all keys/values
                 of __dict__ of the instanc

    """

    lst_str = storage.all()
    prompt = "(hbnb)"
    model_lst = ["BaseModel"]

    def do_create(self, line):
        """ A mehod that print a repesentation of the instance.

        params: None.
        return type: string.
        return value: returns a string representation of the instance.
        """

        if len(line) == 0:
            print("** class name missing **")
        elif line not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            baseex = BaseModel()
            baseex.save()
            print(baseex.id)

    def do_show(self, line):
        lst = line.split()
        if len(lst) < 1:
            print("** class name missing **")
        elif lst[0] not in HBNBCommand.model_lst:
            print("** class doesn't exist **")
        elif len(lst) < 2:
            print("** instance id missing **")
        else:
            inst = lst[0] + "." + lst[1]
            temp = HBNBCommand.lst_str.get(inst)
            if inst:
                print(temp)
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        lst = line.split()
        if len(lst) < 1:
            print("** class name missing **")
        elif lst[0] not in HBNBCommand.model_lst:
            print("** class doesn't exist **")
        elif len(lst) < 2:
            print("** instance id missing **")
        else:
            inst = lst[0] + "." + lst[1]
            temp = HBNBCommand.lst_str.get(inst)
            if inst:
                del HBNBCommand.lst_str[inst]
                print(HBNBCommand.lst_str)
            else:
                print("** no instance found **")

    def do_all(self, line):
        lst = []
        line = line.split()
        if len(line) < 1:
            print("** class doesn't exist **")
        elif line[0] not in HBNBCommand.model_lst:
            print("** class doesn't exist **")
        else:
            for i in HBNBCommand.lst_str:
                lst.append(HBNBCommand.lst_str[i].__str__())
        print(lst)

    def do_update(self, line):
        lst = line.split()
        if len(lst) < 1:
            print("** class name missing **")
        elif lst[0] not in HBNBCommand.model_lst:
            print("** class doesn't exist **")
        elif len(lst) < 2:
            print("** instance id missing **")
        else:
            inst = lst[0] + "." + lst[1]
            temp = HBNBCommand.lst_str.get(inst)
            if inst:
                if len(lst) < 3:
                    print("** attribute name missing **")
                elif (hasattr(temp, "first_name")):
                    print(lst[2])
                else:
                    print("** value missing **")
            else:
                print("** no instance found **")

    def do_quit(self, rest):
        """Exit the program"""
        return True

    def default(self, line):
        """Called for any command not recognized"""
        print("Invalid command:", line)
    
    def completedefault(self, text, line, begidx, endidx):
        """Complete arguments for the hello command"""
        completions = ['hello', 'quit', 'everyone']
        return [c for c in completions if c.startswith(text)]
    
    def do_EOF(self, line):
        """ A mehod that print a repesentation of the instance.

        params: None.
        return type: string.
        return value: returns a string representation of the instance.
        """

        if not line:
            return True
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
