from socket import *

ip_port = ("127.0.0.1", 8000)
buffer_size = 1024

udp_client = socket(AF_INET, SOCK_DGRAM)

udp_client.sendto(b'hello', ip_port)
udp_client.sendto(b"zhenji", ip_port)
udp_client.sendto(b'yanny', ip_port)