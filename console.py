#!/bin/python3
import cmd

class MyCmd(cmd.Cmd):
    def do_hello(self, rest):
        """Say hello"""
        print(len("dfgstagfsgf"))
        print("Hello,", rest)

    def do_quit(self, rest):
        """Exit the program"""
        print("Quitting...")
        return True  # Returning True exits the command loop

    def default(self, line):
        """Called for any command not recognized"""
        print("Invalid command:", line)
    def completedefault(self, text, line, begidx, endidx):
        """Complete arguments for the hello command"""
        completions = ['hello', 'quit', 'everyone']
        return [c for c in completions if c.startswith(text)]
    
    def do_EOF(self, line):
        # Check if the line is empty, which typically signifies EOF
        print(line)
        if not line:
            print("Received EOF. Exiting...")
            return True  # Return True to exit the command loop
        return False  # Continue the command loop
if __name__ == '__main__':
    my_cmd = MyCmd()
    my_cmd.cmdloop() 
