import socket
send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
send.connect(('178.79.134.250', 80))
data = "GET / HTTP/1.1\r\n" + \
       "Host: natas21.natas.labs.overthewire.org\t\n" + \
       "Authorization: Basic bmF0YXMyMTpJRmVrUHlyUVhmdHppREVzVXIzeDIxc1l1YWh5cGRnSg==\r\n"+ \
       "Cookie: cfduid=d022c84dc3a00fd96fe5e208d346fab9a1488448524; __utma=176859643.54228838.1488448531.1488448531.1488525856.2; __utmz=176859643.1488525856.2.2.utmcsr=natas.labs.overthewire.org|utmccn=(referral)|utmcmd=referral|utmcct=/; PHPSESSID=ooqgq3h8q20c36iao7fu4a2fd3\r\n" + \
       "\r\n"
send.send(data.encode())
recv = send.recv(3000)
send.close()
print(recv.decode())
