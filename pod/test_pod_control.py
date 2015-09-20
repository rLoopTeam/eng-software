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
	pod_control.collect_logs()

def test_pod_control_report_state():
	pod_control = PodControl()

	virtual_bus = VirtualBus()
	pod_control.set_bus(virtual_bus)

	pod_control.report_state()

def test_pod_control_hear_message():
	pod_control = PodControl()
	pod_control.hear_message('test')
