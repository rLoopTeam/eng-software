#Console app that lets users issue commands and request tests.

from pod.pod_control import PodControl
from simulation.virtual_bus.virtual_bus import VirtualBus
from systems.nodes.basic_node import BasicNode

# default objects
virtual_bus = VirtualBus()
pod_control = PodControl()

basic_nodes_list = []

#Initialize virtual bus and pod control
pod_control.set_bus(virtual_bus)

#Main menu
print "Choose a test to run, or enter 0 to run all:"
print "0. Add basic node"
print "1. Request State Report"
print "2. Collect Logs"

while True:
    selection = raw_input("Enter your selection: ")
    if selection == "0":
        basic_node = BasicNode()

        basic_nodes_list.append(basic_node)

        basic_node.set_bus(virtual_bus)
        basic_node.register_with_pod_controller()
    elif selection == "1":
        pod_control.report_state()
    elif selection == "2":
        pod_control.collect_logs()
    else:
        print "Invalid selection."