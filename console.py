#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
import inspect
"""
This program contains the entry point of the command interpreter.
"""


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_quit(self, line):
        """
        Command let's you exit the program.
        """
        return True

    def do_EOF(self, line):
        """
        Command to signify end of file.
        """
        return True
    
    def emptyline(self):
        """
        Nothing should be printed on an emptyline.
        """
        pass

    def do_create(self, args):
        """
        Creates an instance of a class.
        """
        if (args):
            if args in globals():
                class_obj = globals().get(args)
                if class_obj:
                    new_cls = class_obj()
                    new_cls.save()
                    print(new_cls.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
    
    def do_show(self, args):
        """
        Prints the string representation of an instance,
        based on the class name and id
        """
        args_list = args.split()
        args_len = len(args_list)
        obj_dict = storage.all()

        if args_len == 0:
            print("** class name missing **")
        elif args_len == 1:
            if args_list[0] not in globals():
                print("** class name doesn't exits **")
            else:
                print("** instance id missing **")
        elif args_len >= 2:
            if args_list[0] in globals():
                if f"{args_list[0]}.{args_list[1]}" not in obj_dict:
                    print("** no instance found **")
                else:
                    print(obj_dict[f"{args_list[0]}.{args_list[1]}"])   


if __name__ == "__main__":
    HBNBCommand().cmdloop()
