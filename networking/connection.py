import requests
import socket

# this class is here for handling all of the request to the actual bridge

# 
def send_command_api(apiAddress, msg):
    adress = "http://" + str(apiAddress) + "/api/" + msg
    print("trying to connect to : ", apiAddress)
    print("with: ", msg)
    return requests.get(adress)

#this can be used later to make more advanced requests if needed
def http_port_test(ip_address, tcp_port, msg):
    buffer_size = 1024

    #the connection part 
    http_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    http_socket.connect((ip_address, tcp_port))
    print("opend TCP Connection to : " , ip_address,":", tcp_port)
    http_socket.send(msg)
    data = http_socket.recv(buffer_size)
    http_socket.close()

    #printing out what we got 
    print("what we recieved: " . data)
    
def getHeaders(ip_address, tcp_port):
    address = "http://"+ip_address.replace(" ", "")+ ":" + tcp_port
    return requests.head(address, data ={'key': 'value'})
