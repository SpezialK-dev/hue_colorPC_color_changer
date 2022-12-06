import networking.connection as con
import sys

confac = con

def __main__():
    print("Welcome")
    #takes an argument and puts it into the connection class
    try:
        #print(con.send_command_api(sys.argv[1], sys.argv[2]))
        http_response_80 = con.getHeaders(sys.argv[1], "80")
        print(http_response_80.headers)
    except:
        print("Something went wrong")

__main__()