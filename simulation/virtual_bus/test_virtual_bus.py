import virtual_bus

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