import uuid

from base import BaseNode
from simulation.virtual_bus.virtual_bus import VirtualBus

class BasicNode(BaseNode):

	def __init__(self):
		self.bus = None
		self.id = uuid.uuid4()

	def setup(self):
		pass

	def loop(self):
		pass

	def set_bus(self, bus):
		self.bus = bus

	def register_with_pod_controller(self):
		registration_message = '%s%s%s' % (VirtualBus.register_node_with_pod_control_message, VirtualBus.message_token_delimiter, self.id)

		self.bus.send_message(registration_message)
