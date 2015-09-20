# pod control system

class PodControl():
	def __init__(self):
		self.bus = None

	def set_bus(self, bus):
		self.bus = bus
		self.bus.add_node(self)

	# external command interface
	def collect_logs(self):
		# TODO: request logs from every registered subsystem
		#myLog = open("commandInterfaceLog.txt", "r")
		#newLog = open("log.txt", "r+")
		#newLog.write("Combined Log" + "\n \n" + myLog.read())
		#for node in nodes:
		#	newLog.write(node.get_log() + "\n \n")
		#log = newLog.read()
		#myLog.close()
		#newLog.close()
		#return log
		print('collect_logs')

	def report_state(self):
		"""Request the current state of every registered sub-system"""
		self.bus.send_message("report_state")


	# subsystem control interface
	def hear_message(self, msg):
		"""Recieve messages from the virtual bus that the pod is attached to."""
		# TODO parse out the message header to determine who the message's sender,
		# intended receiver, and payload. For now just print it.
		print(msg)

