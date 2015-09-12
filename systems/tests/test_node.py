from ..nodes import TestNode
from ..teensy_libs import FlexCAN

def test_register(virtualbus):
    node = TestNode()
    node.CANbus.set_bus(virtualbus)

    fc = FlexCAN(500000, virtualbus)
    fc.begin()

    node.setup()

    assert fc.available() == 1
