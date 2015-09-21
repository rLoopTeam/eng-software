# pod control system

class PodControl:
	#static strings that are known commands. These should not live here:
	register_node_with_pod_control_message = 'register_with_pod_control'

	def __init__(self):
		self.bus = None
		self.node_list = [];

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
		print(msg)

		# TODO parse out the message header to determine who the message's sender,
		# intended receiver, and payload. For now just print it.
		if(msg == PodControl.register_node_with_pod_control_message):
			#todo the list of nodes contained in the pod_controller should be sub system descriptors
			self.node_list.append(msg)


		

		

