import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET = IPv4 , socket.SOCK_STREAM = socket(TCP) , DGRAM = socket(UDP)

server.bind(('192.168.4.100', 8887))
# connection address(host,port)

server.listen(5)
# Number of server listens

print(server.getsockname())
# display my address

# print(server.getpeername())
# display remote address

print(u'waiting for connect...')

connect, (host, port) = server.accept()
#等待client連線,建立連線

peer_name = connect.getpeername()
sock_name = connect.getsockname()
print(u'the client %s:%s has connected.' % (host, port))
print('The peer name is %s and sock name is %s' % (peer_name, sock_name))

while True:
    data = connect.recv(1024)
    # hex_bytes = bytes.fromhex(data)
    hex_string = data.hex()
    print(type(hex_string))
    #接收client的data

    connect.sendall(b'your words has received.')
    print('the client say:' + hex_string)
    # print(hex_string)
    # print(data)


server.close()
