# pod control system

class PodControl:
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
		self.bus = None
		self.node_list = []
		self.node_logs = {}
		self.node_logs_complete = {}

	def set_bus(self, bus):
		self.bus = bus
		self.bus.add_node(self)

	# external command interface
	def collect_logs(self):
		# since nothing is running async at this point, when this method returns
		# all log lines should be available
		self.bus.send_message(PodControl.report_logs_message)

		#write all the log lines recived to a file	
		#myLog = open("commandInterfaceLog.txt", "r")
		newLog = open("log.txt", "r+")
		newLog.write("Combined Log" + "\n \n")
		for node, log_lines in self.node_logs:
			for log_line in log_lines:
				newLog.write('%s -- %s' % (node, log_line))
		#log = newLog.read()
		#myLog.close()
		newLog.close()
		#return log

	def report_state(self):
		"""Request the current state of every registered sub-system"""
		self.bus.send_message(PodControl.report_state_message)


	# subsystem control interface
	def hear_message(self, msg):
		"""Recieve messages from the virtual bus that the pod is attached to."""
		print msg

		# TODO parse out the message header to determine who the message's sender,
		# intended receiver, and payload. For now just print it.
		if(msg.startswith(PodControl.register_node_with_pod_control_message)):
			#todo the list of nodes contained in the pod_controller should be sub system descriptors
			message_tokens = msg.split(PodControl.message_token_delimiter)

			node_id = message_tokens[1]
			
			self.node_list.append(node_id)
			self.node_logs[node_id] = []
			self.node_logs_complete[node_id] = False

		elif(msg.startswith(PodControl.report_node_state_to_pod_control_message)):
			message_tokens = msg.split(PodControl.message_token_delimiter)
			print 'subsystem id:%s, state:%s' % (message_tokens[1], message_tokens[2])

		elif(msg.startswith(PodControl.report_node_log_to_pod_control_message)):
			message_tokens = msg.split(PodControl.message_token_delimiter)

			node_id = message_tokens[1]
			log_line = message_tokens[2]

			self.node_logs[node_id].append(log_line)
			
		elif(msg.startswith(PodControl.report_node_log_to_pod_control_done_message)):
			message_tokens = msg.split(PodControl.message_token_delimiter)

			node_id = message_tokens[1]

			self.node_logs_complete[node_id] = True






		

		

