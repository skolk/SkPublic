import argparse
import time
import os
import cmd

class GenericCLI(cmd.Cmd):
    intro = 'For help type help or ?\
            \nType quit to exit this prompt.\n'

    def do_quit(self, args):
        return True

    def do_exit(self, args):
        return True

    def do_q(self, args):
        return True
    do_EOF = do_quit

class RunCLI(GenericCLI, cmd.Cmd):
    intro ='Welcome.\
            \n to control a system type:\
            \n -aux\
            \n -box\'
        prompt = 'subsystem->'



def printVersionInfo():
    print()
    print("Basic CLI Tool"
    print("Version {} Buid {}".format('1','2')

def parseAndRun():
    parser = argparse.ArgumentParser(description='Launch CLI.')

    #setup launcher
    parser.add_argument("-a", "--aux", help="Launch only aux", action='store_true')
    parser.add_argument("-b", "--box", help="Launch only box", action='store_true')

    args = parser.parse_args()
    printVersionInfo()

    if args.aux:
        AuxCLI().cmdloop()
    elif args.box:
        boxCLI()cmdloop()
    else:
        RunAuxCLI().cmdloop()

if __name__ == "__main__":
    parseAndRun()
