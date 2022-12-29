import networking.connection as cone
import requests
import json


#will show the server info
def server_info(ip_input):
    #will all be in one large 
    con = cone
    try:
        
        server_response = con.getHeaders(ip_input, 80)#will default to 80
        print(server_response.headers)
        #server_header =json.load(server_response.headers)
        #print("connecting to: ", ip_input)
        
        #printing the general variable name
        #for item in server_header:
        #    print(item)

    except:
        print("could not connect to server : ", ip_input)
 
  
