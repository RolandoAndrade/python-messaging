import unittest
import zmq


class MyTestCase(unittest.TestCase):
    def test_client1(self):
        context = zmq.Context()
        socket = context.socket(zmq.DEALER)
        identity = u'worker-%d' % 1
        socket.identity = identity.encode('ascii')
        socket.connect('tcp://localhost:5555')
        print('Client %s started' % identity)
        poll = zmq.Poller()
        poll.register(socket, zmq.POLLIN)
        reqs = 0
        while True:
            reqs = reqs + 1
            print('Req #%d sent..' % reqs)
            socket.send(u'request #%d' % reqs)
            for i in range(10):
                sockets = dict(poll.poll(1000))
                if socket in sockets:
                    msg = socket.recv()
                    print('Client %s received: %s' % (identity, msg))

        socket.close()
        context.term()

    def test_client2(self):
        context = zmq.Context()
        socket = context.socket(zmq.DEALER)
        identity = u'worker-%d' % 2
        socket.identity = identity.encode('ascii')
        socket.connect('tcp://localhost:5555')
        print('Client %s started' % identity)
        poll = zmq.Poller()
        poll.register(socket, zmq.POLLIN)
        reqs = 0
        while True:
            reqs = reqs + 1
            print('Req #%d sent..' % reqs)
            socket.send(u'request #%d' % reqs)
            for i in range(10):
                sockets = dict(poll.poll(1000))
                if socket in sockets:
                    msg = socket.recv()
                    print('Client %s received: %s' % (identity, msg))

        socket.close()
        context.term()


if __name__ == '__main__':
    unittest.main()
