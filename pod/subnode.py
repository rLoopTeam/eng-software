# Sub-Node Prototype, Version 1
# Author: Brett Haines <bhaines418@gmail.com>
# rLoop Software Engineering Team

import uuid
from datetime import datetime

class SubNode():
	# Constructor to define subnode instance variables
	def __init__(self, virtual_bus):
		self.__datetime = datetime.utcnow()
		self.__state = None
		self.__uuid = self.generate_id()
		self.__vBus = virtual_bus
		# Register this subnode with the virtual bus given to it
		self.__vBus.add_node(self)

	def hear_message(self, mesage):
		# TODO: Add message functionality
		pass

	# Generate the UUID.  uuid4 is used, since that is the most random (and
	# therefore, most secure) generation function in the UUID module.
	def generate_id(self):
		if self.__id is None:
			self.__id = uuid.uuid4()

	# Logging function
	def log_current(self):
		return "Time: %s\nState: %s" % (subnode.get_time(), subnode.get_state())

	# Getter functions
	def get_time(self):
		return self.__datetime

	def get_state(self):
		return self.__state

	def get_subnode_id(self):
		return self.__id

	# Setter functions
	def set_time(self, time):
		self.__datetime = time

	def set_state(self, state):
		self.__state = state

# End SubNode class