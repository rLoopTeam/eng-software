import json
import base64

def requirebegin(func):
    def inner(self, *args, **kwargs):
        if not self._begin:
            raise Exception('CAN bus not started')
        return func(self, *args, **kwargs)
    return inner

class CAN_message(object):
    len = 0
    id = 0x0
    buf = ''

    def __str__(self):
        return json.dumps([self.len, int(self.id), base64.b64encode(self.buf)])

    def __unicode__(self):
        return unicode(str(self))

    def set_message(self, data):
        self.len, self.id, self.buf = json.loads(data)
        self.buf = base64.b64decode(self.buf)[:self.len]

    def __eq__(self, other): 
        return str(self) == str(other)

class FlexCAN(object):
    _id = None
    _canbus = None
    _queue = None

    _begin = False

    def __init__(self, baudrate, bus=None):
        if bus:
            self.set_bus(bus)
    
    def set_bus(self, bus):
        self._canbus = bus
        self._queue, self._queue_id = bus.add_listener_queue()

    def begin(self):
        self._begin = True
        pass

    @requirebegin
    def available(self):
        return len(self._queue)

    @requirebegin
    def read(self, msg):
        if self.available() > 0:
            msg.set_message(self._queue.pop(0))
            return True
        return False

    @requirebegin
    def write(self, msg):
        self._canbus.send(str(msg), self._queue_id)
