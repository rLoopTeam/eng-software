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

def test_basic_node_register_with_pod_controller():
	virtual_bus = VirtualBus()

	basic_node = BasicNode()

	basic_node.set_bus(virtual_bus)

	basic_node.register_with_pod_controller()

def test_basic_node_report_state():
	virtual_bus = VirtualBus()

	basic_node = BasicNode()

	basic_node.set_bus(virtual_bus)

	basic_node.hear_message(VirtualBus.report_state_message)

def test_basic_node_report_logs():
	virtual_bus = VirtualBus()

	basic_node = BasicNode()

	basic_node.set_bus(virtual_bus)

	basic_node.hear_message(VirtualBus.report_logs_message)
