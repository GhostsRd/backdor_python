import socket

import time

def inp() :
    text = str(input("  \n \t \t \t ~$ :"))
    send(text)
 
def send(donnee) :
    donnee = donnee.encode('utf8')
    conn.send(donnee)
    connect()

def result() :
    data = conn.recv(1024)
    data = data.decode('utf8')
    print(data)
   
        
        

host,port = ('192.168.0.117',5555)

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.bind((host,port))



print("le serveur est en attente")
socket.listen(5)
conn,adress = socket.accept()
print('client en ligne... \ n',adress[0],':', adress[1])

def connect() :
    while True :
        
        print("Client :",adress[0],"~$ :")
        
        try : 
            result()           
            inp()     
        except :
            result()

      
connect() 
conn.close()
socket.close()