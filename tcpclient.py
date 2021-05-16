import socket
target_srv= "SERVER_ADDRESS" #set this variable
target_port= "SERVER PORT"  #set this variable

#create a socket
my_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect to srv
client.connect((target_srv,target_srv))

#send some test data
client.send("GET / HTTP/1.1\r\nHOST: mytestserver.com\r\n\r\n")

#get response
response = client.receive(4096)

#print response 
print(response)
