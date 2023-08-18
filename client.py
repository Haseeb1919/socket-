import socket


HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
SERVER = SERVER = socket.gethostbyname(socket.gethostname()) 
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect(ADDR)

#funtion to send a msg to the server
def send(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght)) #adding spaces to the msg lenght to make it 64 bytes
    client.send(send_lenght)
    client.send(message)
    print(client.recv(2048).decode(FORMAT)) #printing the msg received from the server

send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello don!")
input()

send("quit") #sending a msg to the server to close the connection

