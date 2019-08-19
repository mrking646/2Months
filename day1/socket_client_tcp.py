from socket import *

ip_port = ("127.0.0.1", 8000)
buffer_size = 4096
back_log = 5

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(ip_port)

while True:
    cmd = input('>>: ').strip()
    if not cmd: continue
    if cmd == 'quit': break

    tcp_client.send(cmd.encode('utf-8'))
    cmd_res = tcp_client.recv(buffer_size)
    print("The result is ", cmd_res.decode('gbk'))
tcp_client.close()