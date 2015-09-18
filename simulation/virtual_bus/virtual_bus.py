import datetime

class VirtualBus(object):

	def __init__(self):
		self.attached_nodes = [];
		self.log_filename =  'virtual_bus_log.txt'
		with open(self.log_filename, 'w') as logfile:
			logfile.write("Begin Log: %s\n" % datetime.datetime.now())

	def add_node(self, node):
		"""Attach a node to the bus.

		A Node is any object that has a method 'hear_message' available for the
		bus to call when one of the attached nodes sends a message to the bus.
		All nodes including the sender will hear the message.
		"""
		self.log_event('appending node %s' % node)
		self.attached_nodes.append(node);

	def print_nodes(self):
		"""Print the nodes attached to the bus"""
		self.log_event('printing nodes.')

		for listener in self.attached_nodes:
			print "Listener: %s" % listener

	def send_message(self, msg):
		"""Send a message to all of the nodes attached to the virtual bus"""
		self.log_event('sending msg %s.' % msg)

		for listener in self.attached_nodes:
			listener.hear_message(msg)

	def log_event(self, event):
		"""Write an event to the log file"""
		event_string = '%s -- %s\n' % (datetime.datetime.now(), event)

		with open(self.log_filename, 'a') as logfile:
			logfile.write(event_string)
