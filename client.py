import socket
import time

host,port = ('localhost',5555)

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


def connecion() :
    try :
        socket.connect((host,port)) 

        print('client est connecter')
    
        while True :
            time.sleep(2)
            x = str(input(' \n \t \t \t ~$ : '))
            x = x.encode('utf8')
            socket.send(x)


            data = socket.recv(1024)
            data = data.decode('utf8')
            print(data) 
    except :
        connecion()
    finally :
        socket.close()
connecion()