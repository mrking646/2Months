from socket import *


udp_client = socket(AF_INET, SOCK_DGRAM)
ip_port = ("127.0.0.1", 8000)
buffer_size = 1024

while True:
    msg = input(">>: ").strip()
    udp_client.sendto(msg.encode('utf-8'), ip_port)
    data, addr=udp_client.recvfrom(buffer_size)
    print("服务器的标准时间是", data.decode('utf-8'))