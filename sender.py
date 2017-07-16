import socket

UDP_IP_FROM_FFMPEG = "127.0.0.1"
UDP_PORT_FROM_FFMPEG = 1234

UDP_IP_TO_RECEIVER = "127.0.0.1"
UDP_PORT_TO_RECEIVER = 5678

sockin = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sockin.bind((UDP_IP_FROM_FFMPEG, UDP_PORT_FROM_FFMPEG))

sockout = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP

while True:
    data, addr = sockin.recvfrom(2048) # buffer size is 1024 bytes
    # print "received message:", data
    print "current stream length is" + str(len(data))
    sockout.sendto(data, (UDP_IP_TO_RECEIVER, UDP_PORT_TO_RECEIVER))

