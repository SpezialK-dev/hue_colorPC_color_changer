import requests

# this class is here for handling all of the request to the actual bridge
def send_command_test(apiAddress):
    adress = "http://" + str(apiAddress) + "/api"
    print("trying to connect to : ", apiAddress)
    print(requests.get(adress))