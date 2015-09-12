# Sub-Node Registration Interface
# Author: Darren Midkiff <d.claymidkiff@gmail.com>
# rLoop Software Engineering Team

#dummy value
nodes = []

def attach_to_bus():
  return


def collect_logs():
  myLog = open("commandInterfaceLog.txt", "r")
  newLog = open("log.txt", "r+")
  newLog.write("Combined Log" + "\n \n" + myLog.read())
  for node in nodes:
  	newLog.write(node.get_log() + "\n \n")
  log = newLog.read()
  myLog.close()
  newLog.close()
  return log

collect_logs()