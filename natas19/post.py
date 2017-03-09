import socket

send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
send.connect(("192.168.0.6", 80))
data = "POST /index_form.php HTTP/1.1 \r\n"
data += "Host: 192.168.0.6\r\n"
data += "Content-Type: application/x-www-form-urlencoded\r\n"
data += "Content-Length: 17\r\n"
data += "\r\n"
data += "value=hello+world"
send.send(data.encode())
recv = send.recv(1500)
recv = recv.decode()
send.close()
print(recv)
