import connection as con
import sys

confac = con

def __main__():
    print("Welcome")
    if(sys.argv[1] != 0):
        con.send_command_test(sys.argv[1])
    else:
        print("awaiting input")

__main__()