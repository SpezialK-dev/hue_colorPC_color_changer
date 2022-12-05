import requests

# this class is here for handling all of the request to the actual bridge

# sends a request
def send_command(apiAddress, msg):
    adress = "http://" + str(apiAddress) + "/api/" + msg
    print("trying to connect to : ", apiAddress)
    print("with: ", msg)
    return requests.get(adress)

#def create_new_user(apiAddress):
    