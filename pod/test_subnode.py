# Sub-Node Testing Functions
# Author: Brett Haines <bhaines418@gmail.com>
# rLoop Software Engineering Team

import subnode

# Pytest Testing functions
def test_logger():
	subnode = SubNode()
	subnode.set_state("Functional")
	assert subnode.log_current() != "Time: \nState: None"

def test_id():
	subnode = SubNode()
	assert subnode.get_subnode_id() is not None