import socket

IP = "192.168.8.103"
PORT = 10000

def host():
    s = socket.socket() # Creating Socket
    s.bind((IP, PORT))  # Binding to Client
    s.listen(5)         # Listening for Response
    print("Listening for response...")
    
    c, t = s.accept()   # Accepting Client
    print("Connected to: {}".format(t))

    message = c.recv(1024).decode('utf-8') # Accepting Message
    print("Client sent: {}".format(message))

    message = message.upper() # Setting All Letters to Capital Letters
    print("Sending to client: {}".format(message))

    c.send(message.encode('utf-8')) # Sending Message to Client
    c.close() # Closing Network with Client
    s.close() # Closing Socket
    return

def client():
    s = socket.socket()
    print("Connecting...")
    
    s.connect((IP, PORT))
    print("Connected.")

    message = input("Enter your message: ")
    s.send(message.encode('utf-8'))     # Sending Message to Server
    print(s.recv(1024).decode('utf-8')) # Recieving Message from Server
    return

def main():
    choice = input("Are you a host or a client (0 / 1): ")
    if choice == '0':
        host()
    elif choice == '1':
        client()
    return

if __name__ == "__main__":
    main()