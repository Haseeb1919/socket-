#server side code 

import socket 
import threading
import sys

#getting ip ad port and header
HEADER = 64
FORMAT = 'utf-8'
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #gets the ip address of the server

#picking the socket 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
ADDR = (SERVER, PORT)

#binding the socket to the server
server.bind(ADDR)


#function to handle the clients
def handle_client(con, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_lenght = con.recv(HEADER).decode(FORMAT) #getting the msg lenght
        msg_lenght = int(msg_lenght)
        msg = con.recv(msg_lenght).decode(FORMAT) #getting the msg
        if msg == "quit":
            connected = False
        print(f"[{addr}] {msg}")
        # con.send("Msg received".encode()) #sending a msg to the client
    con.close()



#function to start the server
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        con, addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (con, addr)) #creating a thread for each client
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")




print ("[STARTING] server is starting...")
start()