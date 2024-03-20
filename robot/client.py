#
#
# #app = Flask(__name__)
#
#
# @app.route("/check")
# def checkworking():
#     return "hello"
#
#
# @app.route("/wheels/<int:value>")
# def getWheelsValue(value):
#     print("v", str(value))
#     if value == 9:
#         value = "worked"
#     return str(value)
#
# app.run(host="0.0.0.0", port= 5000)
#
#
#


import socket
import time

host = socket.gethostname()
port = 8001

connection = (host, port)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(connection)

time =time


def main():
    messages = [
        "Hi.",
        "I am from Montana, where are you from?",
        "Me too, I am from the room we are currently in Bozeman, Montana.",
        "Tango.",
        "What are the odds. Two robots run into to each other from the same state, and the same town, and the same room, with the same name?"
    ]
    for message in messages:
        print("Robot 2 (Client):", message)
        clientSocket.sendall(message.encode())
        data = clientSocket.recv(1024).decode()
        print("Robot 1 (Server):", data)
        time.sleep(1)

    clientSocket.close()


main()