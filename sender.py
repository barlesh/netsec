import socket

UDP_IP_FROM_FFMPEG = "127.0.0.1"
UDP_PORT_FROM_FFMPEG = 1234

UDP_IP_TO_RECEIVER = "10.0.0.1"
UDP_PORT_TO_RECEIVER = 1234

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP_FROM_FFMPEG, UDP_PORT_FROM_FFMPEG))

while True:
    data, addr = sock.recvfrom(2048) # buffer size is 1024 bytes
    print ("received message:", data)
    print( "current stream length is" + str(len(data)))
