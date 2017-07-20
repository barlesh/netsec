import subprocess as subp



def createMovie(vector):
    return False


def createImageMovie(src_image,src_sound, file_name):
    # -re
    command = "ffmpeg  -loop 1  -t 00:00:05 -i " + src_image + " -i " + src_sound + " -r 10 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest -f mpegts " + file_name
    print "createImageMovie: command: \n" + command
    subp.check_call(str(command), shell=True)

def cutMovie(source_file, sec,minute, dest_file):
    command = "ffmpeg -ss 00:" + minute + ":" + sec + " -t 00:00:05 -i " + source_file + " -c copy -vcodec libx264 -f mpegts " + dest_file
    # create file
    print "cutMovie: command: \n" + command
    subp.check_call(str(command), shell=True)



def get_movie_time(j):
    start_sec = 5 * j
    start_min = 0
    if start_sec > 59:
        start_min = start_sec / 60
        start_sec = start_sec % 60
    if start_sec < 10:
        str_sec = "0" + str(start_sec)
    else:
        str_sec = str(start_sec)
    if start_min < 10:
        str_min = "0" + str(start_min)
    else:
        str_min = str(start_min)

    return str_sec, str_min



