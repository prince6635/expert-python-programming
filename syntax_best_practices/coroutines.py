"""
Coroutines:
    A coroutine is a function that can be suspended and resumed, and can have multiple entry points.
    For example, each coroutine consumes or produces data, then pauses until other data are passed along.

    PEP 342 that initiated the new behavior of generators also
    provides a full example on how to create a coroutine scheduler.
    The pattern is called Trampoline, and can be seen as a mediator between coroutines that produce and consume data.
    It works with a queue where coroutines are wired together.

Threading:
    Threading is an alternative to coroutines in Python.
    It can be used to run an interaction between pieces of code.
    But they need to take care of resource locking since they behave in a pre-emptive manner,
    whereas coroutines don't.
"""
from __future__ import with_statement
from contextlib import closing
import socket
import multitask

# simple coroutine test
# The multitask module available at PyPI (install it with easy_install multitask)
# if it doesn't work, download .gz, unzip and then install
# $ tar -xzf multitask-0.2.0.tar.gz
# $ cd multitask-0.2.0
# $ python setup.py install
import time
def coroutine1():
    for i in range(3):
        print 'coroutine1'
        yield i

def coroutine2():
    for i in range(3):
        print 'coroutine2'
        yield i

def test_simple_coroutine():
    multitask.add(coroutine1())
    multitask.add(coroutine2())
    multitask.run()

# complicated coroutine test for sockets and server
def client_handler(sock):
    with closing(sock):
        while True:
            data = (yield multitask.recv(sock, 1024))
            if not data:
                break
            yield multitask.send(sock, data)

def echo_server(hostname, port):
    addrinfo = socket.getaddrinfo(hostname, port, socket.AF_UNSPEC, socket.SOCK_STREAM)
    (family, socktype, proto, canonname, sockaddr) = addrinfo[0]
    with closing(socket.socket(family, socktype, proto)) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(sockaddr)
        sock.listen(5)
        while True:
            multitask.add(client_handler((yield multitask.accept(sock))[0]))

def test_complicated_coroutine():
    hostname = 'localhost'
    port = 1111
    multitask.add(echo_server(hostname, port))
    multitask.run()

if __name__ == '__main__':
    test_simple_coroutine()
    test_complicated_coroutine()
