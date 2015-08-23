# telnet program example
import socket, select, string, sys, random, time, datetime

Host_ID = "HP Laptop"
Ins_ID = "Random_1"
JO_Locator = "JO01GA"
GPS_Coordinates = ["51.0471", "0.5173"]
Station_Info = """
This is a test station for development purposes

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum

"""
Data_Type = 1


#main function
if __name__ == "__main__":
	
	host = "localhost"
	port = 9000
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(20)
	
	# connect to remote host
	try :
		s.connect((host, port))
	except :
		print 'Unable to connect'
		sys.exit()
	
	print 'Connected to remote host. Start sending messages'
	datetime_now = datetime.datetime.utcnow()
	datetime_now_str = datetime_now.strftime("%Y-%m-%dT%H:%M:%S.%f")
	msg = "[00," + datetime_now_str + "," + Host_ID + "," + Ins_ID + "," + JO_Locator + "," + GPS_Coordinates[0] + "," + GPS_Coordinates[1] + "," + Station_Info + "," + str(Data_Type) + "]"
	## Setup info
	s.send(msg)
	while True: # Main sensor loop
		try:
			socket_list = [sys.stdin, s]
			time.sleep(1)
			datetime_now_str = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")
			##Get Data
			msg = "[01," + datetime_now_str + "," + Host_ID + "," + Ins_ID + "," + str(random.random()) + "]"
			#print msg

			s.send(msg)
		except KeyboardInterrupt:
			#s.shutdown(0)
			s.close()
			print "Bye!!"
			sys.exit()

