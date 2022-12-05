import networking.connection as con
import sys

confac = con

def __main__():
    print("Welcome")
    #takes an argument and puts it into the connection class
    try:
        con.send_command(sys.argv[1], sys.argv[2])
        
    except:
        print("you didnt pass enought arguments!!")

__main__()