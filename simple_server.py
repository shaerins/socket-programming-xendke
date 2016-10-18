import sys
import socket

if __name__ == "__main__":
    print("Hello World!")

# 1. Create a socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. "Bind" the socket to an IP and PORT
my_socket.bind(("localhost", 3000))
# 3. Begin "listening" on the socket
my_socket.listen(5)

# 4. Begin "accepting" client connections
conn, addr = my_socket.accept()

def openFile(filename):
    return open(filename, "rb").read()

htmlf = open("inx.html", "rb").read()

# 5. Receive some data (up to 1024 bytes) FROM the client
data = ''
data = conn.recv(1024)
print(data)

data_string = str(data)
get_string = ""

for i in range(0, len(data_string)):
    if(data_string[i:i+4] == "\\r\\n"):
        get_string = data_string[2:i]
        print(get_string)
        break

# TODO: loop through get_string to find filename and serve, filename

if(get_string[0:3] == "GET"):
    conn.sendall(htmlf)
