import socket
from Crypto.Cipher import AES
import wrep
import time
import sys

UDP_IP_FROM_FFMPEG = "127.0.0.1"
UDP_PORT_FROM_FFMPEG = 1234

UDP_IP_TO_RECEIVER = "127.0.0.4"
UDP_PORT_TO_RECEIVER = 5678

encrypt = False
packetSizing = False
rateMatching = False
print "Start"
try:
    if sys.argv[1] == "enc":
        print "encryption mode on"
        encrypt = True
    else:
        encrypt = False
        print "encryption mode off"
except Exception:
    print "no encryption mode chosen. none is default"

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

# encrypt = sys.argv[1]
# packetSizing = sys.argv[2]
# rateMatching = sys.argv[3]


packet_counter = 0



sockin = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sockin.bind((UDP_IP_FROM_FFMPEG, UDP_PORT_FROM_FFMPEG))

sockout = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP

key="'This is a key123'"
iv='This is an IV456'
salt = '!%F=-?Pst970'
key32 = "{: <32}".format(salt).encode("utf-8")
obj = AES.new(key32, AES.MODE_CFB, iv )
# obj = AES.new(key32, AES.MODE_CBC, iv )

print "starting listening to ffmpeg....."
while True:
    data, addr = sockin.recvfrom(2048) # buffer size is 1024 bytes
    print "received data len is:" + str(len(data))
    # data = '4\xd6\x83\x8dd!VT\x92\xaa`A\x05\xe0\x9b\x8b\xf1'
    packet_counter += 1
    send_data = data
    # print "received message:", data
    l = '|'.join(x.encode('hex') for x in data)
    #print l
    if encrypt:
        print "encrypting"
        send_data = obj.encrypt(data)
        print "encrypted data len is:" + str(len(send_data))
    # print "encrypted message:", ciphertext
    l = '|'.join(x.encode('hex') for x in send_data)
    #print l
    if packetSizing:
        send_data = wrep.fakeWrap(send_data)
        print "reszed data len is:" + str(len(send_data))

    # print "sending:" + fakePacket + "\n"
    l = '|'.join(x.encode('hex') for x in send_data)
    #print l
    # msg = "Packet number " + str(packet_counter) + ". current stream length is" + str(len(data)) + ". encrypted len is:" + str(len(ciphertext)) + ". fake len is:" + str(len(fakePacket))
    #msg = "Packet number " + str(packet_counter) + ". current stream length is" + str(len(data)) + ". encrypted len is:" + str(len(ciphertext)) + ". fake len is:" + str(len(fakePacket))"
    # print msg
    sockout.sendto(send_data, (UDP_IP_TO_RECEIVER, UDP_PORT_TO_RECEIVER))
    # time.sleep(10)

