import socket
import time


print("Server is starting up!")
port = 8001
host = socket.gethostname()

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, port))

serverSocket.listen(1)


connection, addr = serverSocket.accept()

print("Server Ready!")

with connection:
    print('Connected by', addr)
    responses = [
        "Hi, you look familiar.",
        "I was just going to say the same thing about you. Where are you from?",
        "Me too. Bozeman, Montana",
        "Me too, wow that is wild. What is your name?",
        "Your not going to believe this, but my name is Tango also.",
        "Looking around this room I'd say pretty high."
    ]
    for response in responses:
        data = connection.recv(1024).decode()
        if not data:
            break
        print("Robot 2 (Client):", data)
        print("Robot 1 (Server):", response)
        connection.send(response.encode())
        time.sleep(1)