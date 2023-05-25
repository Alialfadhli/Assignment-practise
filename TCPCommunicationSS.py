import socket
sock_p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
sock_p.bind(("127.0.0.1",49999))

sock_P.listen(2)
sock_a, sockname= sock_p.accept()

print('Accepted request from', sockname[0],'with port number',sockname[1])

sock_a.close()
sock_p.close()
