#rusty-s3c/cesar

try:
    import socket, argparse, os, sys
except:
    print("Error. You need these libraries installed: \nsocket\nos\nsys")
    exit()
try:
    port = int(sys.argv[1])
except:
    print("Error. Usage: python3 %s <port>" %sys.argv[0])
    exit()

def init_server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #we create a tcp socket
    s.bind(("127.0.0.1", port))
    while True:
        s.listen(300) #listen for connections f
        (cli, addr) = s.accept()
        print("Got a connection from:", addr)
        while True:
            try:
                command = input("command>")
                cli.send(command.encode())
                command_resp = cli.recv(8192)
                print("\nresponse:", command_resp.decode())
            except Exception as e:
                print("Exception:", e, "Exiting...")
                exit()
init_server(port)
