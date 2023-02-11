#!/usr/bin/python3
import cmd
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
        print()
    

if __name__ == "__main__":
    HBNBCommand().cmdloop()
