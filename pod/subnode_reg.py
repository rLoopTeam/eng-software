# Sub-Node Registration Interface
# Author: Brett Haines <bhaines418@gmail.com>
# rLoop Software Engineering Team

import uuid

class SubNode():

	# Upon instantiation, a UUID is generated for the subnode.
	def __init__(self):
		self.__id = None
		self.generate_id()
	
	# Generate the UUID.  uuid4 is used, since that is the most random (and 
	# therefore, most secure) generation function in the UUID module.
	def generate_id(self):
		if self.__id is None:
			self.__id = uuid.uuid4()

	# Returns the subnode's UUID
	def get_subnode_id(self):
		return self.__id

# Testing code:
subnode = SubNode()
print subnode.get_subnode_id()

