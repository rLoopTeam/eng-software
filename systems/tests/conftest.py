import pytest
from ..nodes import *

from multiprocessing import Queue
class VirtualCanBus(object):
    listener_queues = {} 

    def add_listener_queue(self):
        qid = len(self.listener_queues)
        q = []
        self.listener_queues[qid] = q
        return q, qid

    def send(self, msg, queue_id):
        if type(msg) != str:
            raise Exception("Invalid message format")
        
        for qid, q in self.listener_queues.items():
            if qid != queue_id:
                q.append(msg)

@pytest.fixture
def basenode():
    return BaseNode()

@pytest.fixture
def virtualbus():
    return VirtualCanBus()
