import random
import sys
import time
import os
import subprocess as subp

VECTOR_SIZE=36
FILE_PATH = "/home/barlesh/PycharmProjects/netsec/movie.mp4"
IMG_PATH="/home/barlesh/PycharmProjects/netsec/Maccabi_Tel_Aviv.png"
loopback = "127.0.0.1"
loopbackPort = "1234"


vector = [0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0 , 0,0,0,0,0,0, 0,0,0,0,0,0]
for i in range(0,VECTOR_SIZE):
    x = random.randint(0, 1)
    if x == 0 :
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
        minute = 5 * j
        print "minute:" + str(minute)
        hour = 0
        if minute > 59:
            hour = minute / 60
            minute =  divmod(minute, 60)
        if minute < 10:
            str_minute = "0" + str(minute)
        else:
            str_minute = str(minute)
        if hour < 10:
            str_hour = "0" + str(hour)
        else:
            str_hour = str(hour)

        print "minute:" + str_minute
        print "hour:" + str_hour

        ss = "-ss " + str_hour + ":" + str_minute + ":00 "
        command += ss
        command += "-t 00:01:00 "
        file = "-i " + FILE_PATH + " "
        command +=  file
        command += "-c copy -f mpegts "
        dest = "udp://" + loopback + ":" + loopbackPort
        command += dest
        print "executing command: " + command
        # command = "ffmpeg -re -ss 00:01:20 -t 00:01:00 -i /home/barlesh/PycharmProjects/netsec/movie.mp4  -c copy -f mpegts udp://127.0.0.1:1234"
        subp.check_call(str(command), shell=True)
        # os.system(command)
        command = ""
        j += 1
        minute = 0
        hour = 0
        # time.sleep(60*5)

    # case it is 1 (image)
    if item == 1:
        command = "ffmpeg -re -loop 1  -t 00:01:00 "
        file = "-i " + IMG_PATH + " "
        command += file
        command += "-r 10 -vcodec libx264 -f mpegts -b:v 740k "
        dest = "udp://" + loopback + ":" + loopbackPort
        command += dest
        print "executing command:  " + command
        subp.check_call(str(command), shell=True)
        # os.system(command)
        command = ""
        # ffmpeg -re -loop 1  -t 00:05:00 -i /home/barlesh/PycharmProjects/netsec/Maccabi_Tel_Aviv.png -r 10 -vcodec mpeg4 -f mpegts udp://127.0.0.1:1234
        # os.system(command)
        None



