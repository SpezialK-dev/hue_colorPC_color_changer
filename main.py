import networking.networkHeaderParser as parser
import sys


def __main__():
    print("Welcome")
    #takes an argument and puts it into the connection class
    try:
        parser.server_info(sys.argv[1])

        
    except:
        print("Something went wrong")

__main__()