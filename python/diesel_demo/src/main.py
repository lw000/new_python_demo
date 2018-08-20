'''
Created on 2018年5月25日

@author: Administrator
'''

import sys
from diesel import (UDPService, UDPClient, call, send,datagram, quickstart ,receive)

class EchoClient(UDPClient):
    @call
    def say(self, msg):
        send(msg)
        return receive(datagram)
    
class echo_server():   
    while True:
        data = receive(datagram)
        send('you said %s' % data)
        
def echo_client():
    client = EchoClient('localhost', 8013)
    while True:
        msg = raw_input('>')
        print (client.say(msg))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if 'client' in sys.argv[1]:
            quickstart(echo_client)
            raise SystemExit
        elif 'server' in sys.argv[1]:
            quickstart(UDPService(echo_server, 8013))
            raise SystemExit
    print('usage: python %s (server|client)' % sys.argv[0])