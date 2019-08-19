from socket import *
import subprocess

ip_port = ("127.0.0.1", 8000)
buffer_size = 1024
back_log = 5

socket_server_tcp = socket(AF_INET, SOCK_STREAM)
socket_server_tcp.bind(ip_port)
socket_server_tcp.listen(back_log)

while True:
    conn, addr = socket_server_tcp.accept()
    print('New connection...')

    while True:
        try:
            cmd = conn.recv(buffer_size)
            if not cmd: break
            print("The information received is ", cmd.decode('utf-8'))

            res = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                   stderr=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE)

            cd = subprocess.Popen("dir", shell=True,
                                   stderr=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE)

            err = res.stderr.read()


            if err:
                cmd_res = err


            else:
                cmd_res = res.stdout.read()

            if not cmd_res:
                cmd_res = "execute successfully".encode('gbk')

            conn.send(cmd_res)


        except Exception as e:
            print(e)
            break

    conn.close()
