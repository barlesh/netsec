import binascii
import random

buff = "1" * 1472


fakeArray = [1] * 1472
i = 0
for item in fakeArray:
    fakeArray[i] = "1" * i
    i += 1


def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

#FakePacketSize = 1472
FakePacketSize = 1472

def fakeBuff(len1):
    # buff = []
    print "fakeAddBuff:len1 is:", len1
    #buff = [1]*len1

    #for i in range(0,len1):
    #    buff.append(random.randint(0, 5000) % 255)
    print "fakeAddBuff: bufer len is " + str(len(buff))
    return fakeArray[len1]
    #return data + "".join(map(chr, buff))
    # s = data + buff
    # s = s[:1472]
    # return s

def fakeWrap(data):
    len1 = len(data)
    #print "fakeWrap data en is:" + str(len1)
    if len1 == FakePacketSize:
    #    print "packet size == FakePacketSize"
        return data
    strlen = "0000"
    if (len1 < FakePacketSize):
        fake_buff = fakeBuff(FakePacketSize - len1 - 4)
    else:
        return  data

    if len1 < 10:
        strlen = "000" + str(len1)
    else:
        if len1 < 100:
            strlen = "00" + str(len1)
        else:
            if len1 < 1000:
                strlen = "0" + str(len1)
            # len1 > 1000
            else:
                strlen = str(len1)


    # print "strlen is: " + str(strlen)
    # '|'.join(x.encode('hex') for x in strlen)
    strlen2 = int2bytes(len1)
    # print "strlen2 is: " + str(strlen2)
    #'|'.join(x.encode('hex') for x in strlen2)
    # retstr = strlen + fake_buff
    #l = map(chr, fake_buff)
    #if isinstance(l, basestring):
    #    print("l is string")


    return strlen.join([data,fake_buff ])
    #print "retstr is:"
    # '|'.join(x.encode('hex') for x in retstr)
    # return retstr


def fakeUnWrap(fake_data):
    len1 = fake_data[:4]
    #print("fakeUnWrap: len1 is:" + str(len1))
    #l =  '|'.join(x.encode('hex') for x in len1)
    #print l
    try:
        len2 = int(len1)
    except Exception:
        #print "error with number of data len, meaning packet pf size 1472"
        return fake_data
    real_len = len(fake_data)-len2
    #print "real len is:" + str(real_len)
    data = fake_data[4:real_len]
    #print "len of data is: " + str(len(data))
    return data