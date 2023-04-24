#!/usr/bin/python3
import cmd
import argparse
import models
# assuming you have a models module
that defines BaseModel and handles JSON file


class HBNBCommand(cmd.Cmd):
    """A class that contains the entry point of the command interpreter"""

    prompt = "(hbnb) "   # a custom prompt

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    # returns True to stop cmdloop()

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True
    # returns True to stop cmdloop()

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass   # does nothing

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        parser = argparse.ArgumentParser()
        # create an ArgumentParser object
        parser.add_argument('class_name', type=str)
        # add an argument for class name
        args = parser.parse_args(arg.split())
        # parse arguments from arg string
        if args.class_name == "BaseModel":
            # check if class name is valid
            new_instance = models.BaseModel()
            # create a new instance of BaseModel
            new_instance.save()
            # save it to the JSON file
            print(new_instance.id)
            # print its id
        else:
            print("** class doesn't exist **")
            # print error message if class name doesn't exist

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        parser = argparse.ArgumentParser()
        # create an ArgumentParser object
        parser.add_argument('class_name', type=str)
        # add an argument for class name
        parser.add_argument('id', type=str)
        # add an argument for id
        args = parser.parse_args(arg.split())
        # parse arguments from arg string
