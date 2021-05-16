import socket
import threading

serving_ip="0.0.0.0"
serving_port=4444

#create a socket 

server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#set binding 

server.bind((serving_ip,serving_port))
server.listen(5)

#print status

print("[*] Listening %s:%d"% (serving_ip,serving_port))

#thread for handling

def client_thread(client_sock):
    
    #client request
    client_request=client_sock.recv(1024)
    print("[*] Request %s"% (client_request))
    message="Your Message is received successfully"
    client_sock.send(message.encode('utf-8'))
    client_sock.close()
    
while True:
    
    client,addr=server.accept() 
    
    print("[*] Connection Originated From %s:%d"% (addr[0],addr[1]))
    
    client_waiter= threading.Thread(target=client_thread,args=(client,))
    client_waiter.start()
