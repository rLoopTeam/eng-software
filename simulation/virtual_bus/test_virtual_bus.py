import virtual_bus


class MockNode(object):

	def hear_message(self, msg):
		self.msg = msg



def test_create_virtual_bus():
	vb = virtual_bus.VirtualBus()

def test_virtual_bus_add_nodes():
	vb = virtual_bus.VirtualBus()
	vb.add_node(1)
	vb.add_node(2)

def test_virtual_bus_print_nodes(capsys):
	vb = virtual_bus.VirtualBus()
	
	vb.add_node(1)
	vb.add_node(2)

	vb.print_listeners();

	out, err = capsys.readouterr()

	assert out == "Listener: 1\nListener: 2\n"

def test_virtual_bus_send_message():
	vb = virtual_bus.VirtualBus()

	mock_nodes = [MockNode(), MockNode(), MockNode()]

	for node in mock_nodes:
		vb.add_node(node)

	test_msg = 1

	vb.send_message(test_msg)

	for node in mock_nodes:
		assert node.msg == test_msg
