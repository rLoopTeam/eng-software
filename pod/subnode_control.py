# Sub-Node Command Interface
# Author: Brett Haines <bhaines418@gmail.com>
# rLoop Software Engineering Team

from datetime import datetime

class SubNode():
	
	# Constructor to define subnode instance variables
	def __init__(self):
		self.__datetime = datetime.datetime.utcnow()
		self.__state = None

	# Getter functions
	def get_time(self):
		return self.__datetime

	def get_state(self):
		return self.__state

	# Setter functions
	def set_time(self, time):
		self.__datetime = time

	def set_state(self, state):
		self.__state = state

