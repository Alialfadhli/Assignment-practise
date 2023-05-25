import socket
number = '0123456789'
Char = 'A_Z'
Sympol = '0@#%$'

ss = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
ss.bind(("127.0.0.1" , 49999))
data, address  = ss.recvfrom(2048)

print('Received: ', data.decode('ascii'))

if data.decode('asci')=='Num':
    ss.sendto(number.encode('ascii'),address)
elif data.decode('asci') == 'Char':
    ss.sendto(Char.encode('ascii'), address)
elif data.decode('ascii')=='Smp':
    ss.sendto(Sympol.encode('ascii'), address)

ss.close()