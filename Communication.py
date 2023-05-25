import socket
cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = input("Send")

cs.sendto(msg.encode('ascii'),('127.0.0.1',49999))
data, address = cs.recvfrom(2048)
print('Received: ', data.decode('ascii'))
Yazeed 3mk
cs.close