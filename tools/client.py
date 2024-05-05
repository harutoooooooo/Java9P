import sys
import socket
from p9 import *

def main():
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]:s} <HOST> <PORT>')
        exit(1)
    
    io = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    io.connect((sys.argv[1], int(sys.argv[2], 10)))

    # version
    io.send(encode_Tversion(-1, 0x2000, b'9P2000'))
    decode_msg(io.recv(1024))

    # attach
    io.send(encode_Tattach(0, 0, -1, b'riruoda', b''))
    decode_msg(io.recv(1024))

    # stat
    io.send(encode_Tstat(0, 0))
    decode_msg(io.recv(1024))

if __name__ == '__main__':
    main()