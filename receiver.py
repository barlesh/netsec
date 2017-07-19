import socket
from Crypto.Cipher import AES
import wrep
import sys

UDP_IP_FROM_SENDER = "127.0.0.4"
UDP_PORT_FROM_SENDER = 5678

UDP_IP_TO_FFMPEG = "127.0.0.3"
UDP_PORT_TO_FFMPEG = 9012

decrypt = False
packetSizing = False
rateMatching = False

try:
    if sys.argv[1] == "dec":
        print "decryption mode on"
        decrypt = True
    else:
        decrypt = False
        print
        "decryption mode off"
except Exception:
    print "no decryption mode chosen. none is default"

try:
    if sys.argv[2] == "packresize":
        print "resize mode on"
        packetSizing = True
    else:
        packetSizing = False
        print "resize mode off"
except Exception:
    print "no packet resizing mode chosen. none is default"

try:
    if sys.argv[3] == "ratematch":
        print "rate match mode on"
        rateMatching = True
    else:
        rateMatching = False
        print "rate match mode off"
except Exception:
    print "no rate matching mode chosen. none is default"



sockin = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sockin.bind((UDP_IP_FROM_SENDER, UDP_PORT_FROM_SENDER))

sockout = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP

key="'This is a key123'"
iv='This is an IV456'
salt = '!%F=-?Pst970'
key32 = "{: <32}".format(salt).encode("utf-8")
obj = AES.new(key32, AES.MODE_CFB, iv )
# obj = AES.new(key32, AES.MODE_CBC, iv )

while True:
    data, addr = sockin.recvfrom(2048) # buffer size is 1024 bytes
    print "received data len is:" + str(len(data))
    # print "received message:", cypherdata
    if packetSizing:
        data = wrep.fakeUnWrap(data)
        print "resized data len is:" + str(len(data))

    if decrypt:
        data = obj.decrypt(data)
        print "decrypted data len is:" + str(len(data))

    if not data:
        print "no len at data, so it is of size 1472"
        #continue

    # print "current stream (cyphered) length is" + str(len(cypherdata)) + ". fake_data_len is:" + str(len(fake_data)) + ". data: " + str(len(data))
    sockout.sendto(data, (UDP_IP_TO_FFMPEG, UDP_PORT_TO_FFMPEG))
    print "done"