"""
 	Name: 		setnet
 	Version:	0.1 
 	Author:		Antares
 	Modified:	26.12.13
 	
 	This application provides access over telnet and runs commands on devices. 
 	The devices and commmands used are read in over files (device_list,
 	command_list)

	!!!Important!!!: the command_list always needs to start with "terminal length 0"
	otherwise the "more" command will wait for input from user!

 	Supported devices: Cisco
  
	#Todo: 
"""
import sys
from j_connect import TnCiscoAccess

if __name__ == "__main__": 
	if len(sys.argv) != 3:
		raise SystemExit("Usage: python setnet.py (uid) (pw)")
	uid = str(sys.argv[1])
	pw = str(sys.argv[2])

	fh_device_list = open ('./device_list', 'r')
	fh_command_list = open ('./command_list', 'r')
	commandlist = [line for line in fh_command_list]

	for line in fh_device_list:
		device = line.split()
		host = device [0]
		ip = device[1]

	 	print "\n\n" + host + ": " + ip  + ":\n======================\n"
	 	#connect to device
		tn_session = TnCiscoAccess(ip, host, uid, pw)
		tn_session.ios_enable_acs_bug(host) #acs bug, see j_connect
		#run commands
		terminal_output = tn_session.run_command(commandlist)
		print terminal_output
		tn_session.closeTCA()
