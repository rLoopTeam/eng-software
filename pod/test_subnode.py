# Sub-Node Testing Functions
# Author: Brett Haines <bhaines418@gmail.com>
# rLoop Software Engineering Team

from subnode import SubNode
from simulation.virtual_bus.virtual_bus import VirtualBus


# Pytest Testing functions
def test_logger():
	virtualbus = VirtualBus()
	subnode = SubNode(virtualbus)
	subnode.set_state("Functional")
	assert subnode.log_current() != "Time: \nState: None"

def test_id():
	virtualbus = VirtualBus()
	subnode = SubNode(virtualbus)
	assert subnode.get_subnode_id() is not None
