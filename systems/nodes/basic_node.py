import uuid

from base import BaseNode
from simulation.virtual_bus.virtual_bus import VirtualBus
from systems.Systems_InternalStateManager import InternalStateManager

class BasicNode(BaseNode):

	
	def __init__(self):
		self.bus = None
		self.id = uuid.uuid4()
		self.ISM = InternalStateManager()

	def setup(self):
		pass

	def loop(self):
		pass

	def set_bus(self, bus):
		self.bus = bus
		self.bus.add_node(self)

	def register_with_pod_controller(self):
		registration_message = '%s%s%s' % (VirtualBus.register_node_with_pod_control_message, VirtualBus.message_token_delimiter, self.id)

		self.bus.send_message(registration_message)

	def hear_message(self, msg):
		"""Recieve messages from the virtual bus that the pod is attached to."""
		print msg

		# there are only two messages that the basic node will respond to. A
		# request for node state and a request for logs
		
		if(msg.startswith(VirtualBus.report_state_message)):
			# respond to the request for state with a fake state
			# TODO: hook up the internal state manager to this node

			state_message = VirtualBus.report_node_state_to_pod_control_message
			state_message += VirtualBus.message_token_delimiter
			state_message += str(self.id)
			state_message += VirtualBus.message_token_delimiter
			state_message += str(self.ISM.ISM_GetCurrentState())

			self.bus.send_message(state_message)


		elif(msg.startswith(VirtualBus.report_logs_message)):
			# respond to the request for logs with multiple fake log messages
			# TODO: store actual logs and return them when requested

			for i in range(0, 10):
				log_message = self.generate_log_message(str(i))
				self.bus.send_message(log_message)

			complete_log_sending_message = VirtualBus.report_node_log_to_pod_control_done_message
			complete_log_sending_message += VirtualBus.message_token_delimiter
			complete_log_sending_message += str(self.id)

			self.bus.send_message(complete_log_sending_message)
	
	def get_state(self):
		return self.ISM.ISM_GetCurrentState()

	def generate_log_message(self, log_contents):
		log_message = VirtualBus.report_node_log_to_pod_control_message
		log_message += VirtualBus.message_token_delimiter
		log_message += str(self.id)
		log_message += VirtualBus.message_token_delimiter
		log_message += log_contents

		return log_message

