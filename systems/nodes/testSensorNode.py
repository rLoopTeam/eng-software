from base import BaseNode

class TestSensorNode(BaseNode):
    def __init__(self, id):
        self.current_task = None
        self.id = id

    def setup(self, virtual_bus):
        virtual_bus.add_node(self)

    def loop(self):
        pass

    def hear_message(self, msg):
        print('%s: Received message. Now check if we need to respond.'%self.id)
        print('%s - message: %s'%(self.id, msg))
        msg_parts = msg.split(' ')
        
        """
        msg_parts contains the message components. 
        e.g.    [0] the message itself (which is just a command)
                [1] the id (need to check if id matches current node to see if this node needs to do anything)
        """
        if msg_parts[1] == self.id:
            print('%s: This message is for us. Do something'%self.id)
            self.current_task = msg_parts[0]

