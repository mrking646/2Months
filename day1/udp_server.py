from socket import *

ip_port = ("127.0.0.1", 8000)
buffer_size = 1024

udp_server = socket(AF_INET, SOCK_DGRAM)
udp_server.bind(ip_port)




data1 = udp_server.recvfrom(buffer_size)
data2 = udp_server.recvfrom(buffer_size)
data3 = udp_server.recvfrom(buffer_size)


print(data1)
print(data2)
print(data3)