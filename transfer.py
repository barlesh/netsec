import random
import sys
import time
import os
import subprocess as subp
import movie

VECTOR_SIZE=36
# FILE_PATH = "/home/barlesh/PycharmProjects/netsec/movie.mp4"
FILE_PATH = "/home/barlesh/PycharmProjects/netsec/Coldplay-UpUp.mp4"

# IMG_PATH="/home/barlesh/PycharmProjects/netsec/Maccabi_Tel_Aviv.png"
IMG_PATH="/home/barlesh/PycharmProjects/netsec/636035800177516681RA.jpg"
loopback = "127.0.0.1"
loopbackPort = "1234"


vector = [0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0 , 0,0,0,0,0,0, 0,0,0,0,0,0]
for i in range(0,VECTOR_SIZE):
    x = random.randint(0, 10)
    if x < 10 :
    # if x == 0:
        x1 = 0
    else:
        x1 = 1
    # print "i:" + str(i)
    vector[i] = x1

print "vector:"
j = 0


for item in vector:
    print "item " + str(j) + ": " + str(item)


    # case it is 0 (movie)
    if item == 0:
        command = "ffmpeg -re "
        start_sec = 5 * j
        print "start_sec:" + str(start_sec)
        start_min = 0
        if start_sec > 59:
            start_min = start_sec / 60
            start_sec =  start_sec % 60
        if start_sec < 10:
            str_sec = "0" + str(start_sec)
        else:
            str_sec = str(start_sec)
        if start_min < 10:
            str_min = "0" + str(start_min)
        else:
            str_min = str(start_min)

        print "minute:" + str_min
        print "second:" + str_sec

        ss = "-ss " + "00:" + str_min + ":" + str_sec + " "
        command += ss
        command += "-t 00:00:05 "
        file = "-i " + FILE_PATH + " "
        command +=  file
        command += "-c copy -f mpegts "
        dest = "udp://" + loopback + ":" + loopbackPort
        command += dest
        # command += " 2> /dev/null"
        print "executing command: " + command
        # command = "ffmpeg -re -ss 00:01:20 -t 00:01:00 -i /home/barlesh/PycharmProjects/netsec/movie.mp4  -c copy -f mpegts udp://127.0.0.1:1234"
        subp.check_call(str(command), shell=True)
        print "Done!"

    # case it is 1 (image)
    if item == 1:
        command = "ffmpeg -re -loop 1  -t 00:00:05 "
        file = "-i " + IMG_PATH + " "
        command += file
        # command += "-r 10 -vcodec libx264 -f mpegts -b:v 740k "
        command += "-r 10 -vcodec libx264 -f mpegts  "
        dest = "udp://" + loopback + ":" + loopbackPort
        command += dest
        # command += " 2> /dev/null"
        print "executing command:  " + command
        subp.check_call(str(command), shell=True)
        print "Done!!!!"
        # ffmpeg -re -loop 1  -t 00:05:00 -i /home/barlesh/PycharmProjects/netsec/Maccabi_Tel_Aviv.png -r 10 -vcodec mpeg4 -f mpegts udp://127.0.0.1:1234

        None
    j += 1
    minute = 0
    hour = 0
    command = ""
    time.sleep(0.5)


