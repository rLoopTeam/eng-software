from base import BaseNode
from ..teensy_libs.flexcan import *

class TestNode(BaseNode):
    CANbus = FlexCAN(500000)

    ID = 255 
    registered = False

    def setup(self):
        self.CANbus.begin()

        # register node
        msg =  CAN_message()
        msg.id = self.CANMSG_REGISTER
        msg.len = 1
        msg.buf = chr(self.ID)
        self.CANbus.write(msg)

    def loop(self):
        pass


