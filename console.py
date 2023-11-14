#!/usr/bin/python3
"""Defines the HBnB console."""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage as storage
import cmd
import re
from shlex import split


def parse(arg):
    """
    Parses the input string to extract content within curly
    braces {} or square brackets [].

    Args:
        arg (str): The input string to be parsed.

    Returns:
        list: A list containing the parsed elements.

    Example:
        >>> parse("This is a {sample} string with [some, elements].")
        ['This is a ', 'sample', ' string with ', 'some', ', elements', '.']
    """
    # Use regular expressions to search for content within
    # curly braces and square brackets
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)

    # Check if there are no curly braces in the input string
    if curly_braces is None:
        # If there are also no square brackets
        if brackets is None:
            # Assuming split is defined elsewhere
            return [char.strip(",") for char in split(arg)]
        else:
            # If square brackets are found
            lexer = split(arg[:brackets.span()[0]])
            passed_list = [i.strip(",") for i in lexer]
            passed_list.append(brackets.group())
            return passed_list
    else:
        # If curly braces are found
        lexer = split(arg[:curly_braces.span()[0]])
        passed_list = [i.strip(",") for i in lexer]
        passed_list.append(curly_braces.group())
        return passed_list


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """
        Default behavior for cmd module when input is invalid.

        Args:
            arg (str): The input argument string.
        """
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            passed_arg = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", passed_arg[1])
            if match is not None:
                command = [
                        passed_arg[1][:match.span()[0]],
                        match.group()[1:-1]
                        ]
                if command[0] in argdict.keys():
                    call = "{} {}".format(passed_arg[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        Args:
            arg (str): The input argument string.

        Returns:
            bool: True to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program.

        Args:
            arg (str): The input argument string.

        Returns:
            bool: True to exit the program.
        """
        print("")
        return True

    def do_create(self, arg):
        """
        Create a new class instance and print its id.

        Args:
            arg (str): The input argument string.
        """
        passed_arg = parse(arg)
        if len(passed_arg) == 0:
            print("** class name missing **")
        elif passed_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(passed_arg[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        Display the string representation of a class
        instance of a given id.

        Args:
            arg (str): The input argument string.
        """
        passed_arg = parse(arg)
        objdict = storage.all()
        if len(passed_arg) == 0:
            print("** class name missing **")
        elif passed_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(passed_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(passed_arg[0], passed_arg[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(passed_arg[0], passed_arg[1])])

    def do_destroy(self, arg):
        """
        Delete a class instance of a given id.

        Args:
            arg (str): The input argument string.
        """
        passed_arg = parse(arg)
        objdict = storage.all()
        if len(passed_arg) == 0:
            print("** class name missing **")
        elif passed_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(passed_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(
                passed_arg[0],
                passed_arg[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(passed_arg[0], passed_arg[1])]
            storage.save()

    def do_all(self, arg):
        """
        Display string representations of all instances of a given class.

        Args:
            arg (str): The input argument string.
        """
        passed_arg = parse(arg)
        if len(passed_arg) > 0 and passed_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(
                        passed_arg
                        ) > 0 and passed_arg[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(passed_arg) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        """
        Retrieve the number of instances of a given class.

        Args:
            arg (str): The input argument string.
        """
        passed_arg = parse(arg)
        count = 0
        for obj in storage.all().values():
            if passed_arg[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Update a class instance of a given id by adding or
        updating a given attribute key/value pair or dictionary.

        Args:
            arg (str): The input argument string.
        """
        passed_arg = parse(arg)
        objdict = storage.all()

        if len(passed_arg) == 0:
            print("** class name missing **")
            return False
        if passed_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(passed_arg) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(passed_arg[0], passed_arg[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(passed_arg) == 2:
            print("** attribute name missing **")
            return False
        if len(passed_arg) == 3:
            try:
                type(eval(passed_arg[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(passed_arg) == 4:
            obj = objdict["{}.{}".format(passed_arg[0], passed_arg[1])]
            if passed_arg[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[passed_arg[2]])
                obj.__dict__[passed_arg[2]] = valtype(passed_arg[3])
            else:
                obj.__dict__[passed_arg[2]] = passed_arg[3]
        elif type(eval(passed_arg[2])) == dict:
            obj = objdict["{}.{}".format(passed_arg[0], passed_arg[1])]
            for k, v in eval(passed_arg[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
