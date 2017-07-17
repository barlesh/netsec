from enc import enc

PACKET_SIZE=16*128
SIZE_FIELD_SIZE=4

def encapsulatePacket(data):
    leng = len(data)
    tail = range(1, PACKET_SIZE - leng - SIZE_FIELD_SIZE)
    return enc(leng + data + tail)


def decapsulatePacket(data):

