from base import BaseNode

class BasicNode(BaseNode):

	def __init__(self):
		self.bus = None

	def setup(self):
		pass

	def loop(self):
		pass

	def set_bus(self, bus):
		self.bus = bus
