import pytest
from ..teensy_libs.flexcan import *


def test_requirebegin():
    fc = FlexCAN(500000)
    with pytest.raises(Exception) as excinfo:
        fc.available() 
    assert str(excinfo.value) == 'CAN bus not started'

def test_send(virtualbus):
    a = FlexCAN(500000, virtualbus)
    b = FlexCAN(500000, virtualbus)
    
    a.begin()
    b.begin()

    txmsg = CAN_message()
    rxmsg = CAN_message()

    txmsg.len = 8
    txmsg.id = 0x222
    txmsg.buf = '12345678'

    a.write(txmsg)
    assert a.available() == 0
    assert b.available() == 1

    b.read(rxmsg)
    assert txmsg == rxmsg
