

class VirtualBus(object):

	def __init__(self):
		self.attached_nodes = [];

	def add_node(self, node):
		"""Attach a node to the bus.

		A Node is any object that has a method 'hear_message' available for the
		bus to call when one of the attached nodes sends a message to the bus.
		All nodes including the sender will hear the message.
		"""

		self.attached_nodes.append(node);

	def print_nodes(self):
		"""Print the nodes attached to the bus"""
		for listener in self.attached_nodes:
			print "Listener: %s" % listener

	def send_message(self, msg):
		"""Send a message to all of the nodes attached to the virtual bus"""
		for listener in self.attached_nodes:
			listener.hear_message(msg)



