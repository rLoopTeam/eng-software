from base import BaseNode

class TestSensorNode(BaseNode):
    def __init__(self, id):
        self.log = ['LOG:=== START ===']
        self.current_task = None
        self.id = id
    
    def logger(self, log):
        self.log.append(log)

    def setup(self, virtual_bus):
        virtual_bus.add_node(self)
        self.logger('LOG:%r - INFO: Registered'%self.id)

    def loop(self):
        pass

    def hear_message(self, msg):
        self.logger('LOG:%r - INFO: Received message. Now check if we need to respond.'%self.id)
        self.logger('LOG:%r - MESSAGE: %r'%(self.id, msg))
        msg_parts = msg.split(' ')
        
        """
        msg_parts contains the message components. 
        e.g.    [0] the message itself (which is just a command)
                [1] the id (need to check if id matches current node to see if this node needs to do anything)
        """
        if msg_parts[1] == self.id:
            self.logger('LOG:%r - INFO: This message is for us. Run task: %r'%(self.id, msg_parts[0]))
            self.current_task = msg_parts[0]
            try:
                getattr(self, str(msg_parts[0]))()
            except Exception, e:
                raise
        else:
            self.logger('LOG:%r - INFO: Message not for us. Ignore.')

    """
    Commands - These are the functions that can be run from a message
    """
    def get_log(self):
        self.logger('LOG:%r - TASK: get_log. Return log'%self.id)
        formatted_log = '\n'.join(self.log)
        #print(formatted_log)
        #self.current_task = None
        return formatted_log




