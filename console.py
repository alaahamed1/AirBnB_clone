#!/usr/bin/python3
"""
Console 0.0.1  that contains the entry point of the command interpreter
"""

import cmd
import sys

from models.user import User

class HBNBCommand(cmd.Cmd):
	"""The main cmd of the program for testing
	 and adminstrative purposes"""

	prompt = "(hbnb) "
	def do_quit(self, arg):
		"""Quit command to exit the program"""
		return True

	def do_EOF(self, arg):
		"""EOF command to exit the program"""
		print("")
		return True

	def emptyline(self):
		"""Do nothing on an empty input line"""
		pass
	
	
	def do_create(self, arg):
		"""
		Creates a new instance of the specified model class,
		saves it (to the JSON file), and prints the id.

		Ex: $ create User email="john.doe@example.com" password="MyStrongPassword"
		"""
		if not arg:
			print("** class name missing **")
		elif arg not in self.classes:
			print("** class doesn't exist **")
		else:
			class_name = arg
			new_instance = getattr(sys.modules[__name__], class_name)()
			arg_dict = {}
			for arg_pair in arg.split()[1:]:
				key, value = arg_pair.split("=")
				arg_dict[key] = value
			for key, value in arg_dict.items():
				setattr(new_instance, key, value)
			new_instance.save()
			print(new_instance.id)
if __name__ == '__main__':
	HBNBCommand().cmdloop()
