

class VirtualBus(object):

	def __init__(self):
		self.listeners = [];

	def add_node(self, node):
		self.listeners.append(node);

	def print_listeners(self):
		for listener in self.listeners:
			print "Listener: %s" % listener


