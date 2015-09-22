import datetime

class VirtualBus(object):
	#static strings that are known commands. These should not live here:
	message_token_delimiter = ';'
	register_node_with_pod_control_message = 'register_with_pod_control'

	# state report message prefix. Full message expected to be in the form:
	# subsystem_state_report;<sub_system_id>;<state>
	report_node_state_to_pod_control_message = 'subsystem_state_report'

	# log report message prefix. Full message expected to be in the form:
	# subsystem_log_report;<sub_system_id>;<log>
	report_node_log_to_pod_control_message = 'subsystem_log_report'

	# state report message prefix. Full message expected to be in the form:
	# subsystem_log_report_done;<sub_system_id>
	report_node_log_to_pod_control_done_message = 'complete_subsystem_log_report'

	report_state_message = 'report_state'
	report_logs_message = 'report_logs'
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
