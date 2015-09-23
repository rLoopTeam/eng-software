# tests for the BasicNode

from ..nodes.basic_node import BasicNode

from simulation.virtual_bus.virtual_bus import VirtualBus

def test_basic_node_creation():
	basic_node = BasicNode()
	assert basic_node != None

def test_basic_node_set_bus():
	virtual_bus = VirtualBus()

	basic_node = BasicNode()

	basic_node.set_bus(virtual_bus)

	assert basic_node.bus == virtual_bus