from ..nodes.testSensorNode import TestSensorNode
from simulation.virtual_bus.virtual_bus import VirtualBus

def test_sensor_register(virtualbus):
    node = TestSensorNode('external_temp_node')
    bus = VirtualBus()

    """
    Register node
    """
    print(' ')
    print(' ')
    print('TEST: Register node')
    node.setup(bus)

    """
    Registered?
    """
    node_is_attached = False
    for a_node in bus.attached_nodes:
        if a_node.id == node.id:
            node_is_attached = True
    assert node_is_attached
    print('SUCCESS: Registered')

    """
    Check state of log
    """
    print(' ')
    print(node.get_log())
    print(' ')
    assert len(node.log) == 3 #length of log at node registration

    """
    Send the get_log message
    """
    msg_reg = 'get_log %s'%(node.id)
    bus.send_message(msg_reg)


    """
    Did node receive message?
    """
    print( 'TEST: Did %r hear message?'%node.id)
    assert node.current_task
    print('SUCCESS: Received message')

    print(' ')
    print(node.get_log())

