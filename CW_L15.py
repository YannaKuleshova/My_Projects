#########################
#Author: Kuleshova Yana
#Date: 18/12/2021
#Task: CW to L15
#########################

# Class Work - pytest
import pytest

def add5(v):
    myval = v + 5
    return myval

def test_add5():
    r = add5(1)
    assert r == 6
    r = add5(5)
    assert r == 10
    r = add5(10.102645)
    
# Class Work - unittest !
import unittest

def add5(v):
    myval = v + 5
    return myval

class test_add5(unittest.TestCase):
    def test_add5(self):
        self.assertEqual(add5(1), 6)
        self.assertEqual(add5(5), 10)
        self.assertEqual(add5(10.102645), 15.102645)

if __name__ == '__main__':
    unittest.main()

# Class Work - Site checker
import sys
import socket

if len(sys.argv) not in [2,3]:
    print('Improper nnumber of arguments: at least one is'\
        + 'and not more than two are allowed: ')
    print('- http server\'s adress (required)')
    print(' - port number (defaults to 80 if not specifield)')
    exit(1)

addr = sys.argv[1]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) == 3:
    try:
        port = int(sys.argv[2])
        if not (1 <= port <= 65535):
            raise ValueError
    except ValueError:
        print("Port nummber is invalid - exiting.")
        exit(2)

else:
    port = 80

try:
    sock.connect(addr, port)
except socket.timeout:
    print("The server" + addr + "seems to be dead - sorry.")
    exit(3)
except socket.gaierror:
    print("Server adress" + addr + "is invalid or malformed - sorry.")
    exit(4)

request = b"HEAD / HTTP/1.0\r\nHost: " + \
        bytes(addr, "utf8") + \
        b"\r\nConnection:close\r\n\r\n"

sock.send(request)
answer = sock.recv(100).decode("utf8")
sock.shutdown(socket.SHUT_RDWR)
sock.close()
print(answer[:answer.find('\r')])
