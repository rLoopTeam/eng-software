#test for the pod control system
from pod_control import PodControl
from simulation.virtual_bus.virtual_bus import VirtualBus

# Pytest Testing functions
def test_pod_control_createion():
	pod_control = PodControl()

def test_pod_control_set_bus():
	pod_control = PodControl()

	virtual_bus = VirtualBus()
	pod_control.set_bus(virtual_bus)

def test_pod_control_collect_logs():
	pod_control = PodControl()

	virtual_bus = VirtualBus()
	pod_control.set_bus(virtual_bus)

	pod_control.collect_logs()

def test_pod_control_report_state():
	pod_control = PodControl()

	virtual_bus = VirtualBus()
	pod_control.set_bus(virtual_bus)

	pod_control.report_state()

def test_pod_control_hear_message():
	pod_control = PodControl()
	pod_control.hear_message('test')

def test_pod_control_hear_message_subsytem_state_report():
	test_report_string = 'subsystem_state_report;test_id;test_state'

	pod_control = PodControl()
	pod_control.hear_message(test_report_string)

def test_pod_control_register_sub_system():
	test_string = 'register_with_pod_control;test_id'
	pod_control = PodControl()
	pod_control.hear_message(test_string)

	assert(len(pod_control.node_list) == 1)
	assert(pod_control.node_list[0] == 'test_id')