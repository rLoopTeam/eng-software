import command_interface

def test_collect_logs():
	print command_interface.collect_logs()
	assert isinstance(command_interface.collect_logs(),str)