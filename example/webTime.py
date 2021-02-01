import socket
import time
from flask import Flask, json

api = Flask(__name__)


def TimefromNtp(addr='0.de.pool.ntp.org'):
    REF_TIME_1970 = 2208988800      # Reference time
    client = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    data = b'\x1b' + 47 * b'\0'
    client.sendto( data, (addr, 123))
    data, address = client.recvfrom( 1024 )
    if data:
        t = int.from_bytes(data[32:36], byteorder="big", signed=False)
        t -= REF_TIME_1970
    return time.ctime(t)


@api.route('/time', methods=['GET'])
def get_time():
    return json.dumps("[{time=%s}]" % TimefromNtp())


if __name__ == '__main__':
    api.run(host="0.0.0.0", port=int("8080"))