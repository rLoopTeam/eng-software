from ..nodes.testSensorNode import TestSensorNode
from simulation.virtual_bus.virtual_bus import VirtualBus

def test_sensor_register(virtualbus):
    node = TestSensorNode('external_temp_node')
    bus = VirtualBus()

    node.setup(bus)
    msg_reg = 'get_log %s'%(node.id)
    bus.send_message(msg_reg)

    """
    Registered?
    """
    node_is_attached = False
    for a_node in bus.attached_nodes:
        if a_node.id == node.id:
            node_is_attached = True
    assert node_is_attached


    """
    Did node receive message?
    """
    print( ('Bus: Did %r hear message? %r')%(node.id, node.current_task))
    assert node.current_task
