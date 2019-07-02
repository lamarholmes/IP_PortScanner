#Port Scanner - Checking for Open Ports on IP
#Documentation on Sockets : https://docs.python.org/2/howto/sockets.html
import socket
import sys

ipAddress = input("Please enter IP address: ")

print("Please choose your range of ports, take memory into account")
startPort = int(input("Please give a starting port: "))
EndPort = int(input("Please give the final port: "))

print("Thank you! Now scanning {} from {} to {}".format(ipAddress,startPort,EndPort))

try:
	for port in range(startPort,EndPort):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		openPort = s.connect_ex((ipAddress, port))
		if openPort == 0:
			print("Port {}: is Open".format(port))
			s.close()

#If its not a good IP
except socket.gaierror:
	print("IP is probably not real")
	sys.exit()
#If a connection is refused or you 
except socket.error:
	print("Couldn't connect to server")
	sys.exit()

#If user stops the scan
except KeyboardInterrupt:
    print("You chose to exit scan")
    sys.exit()

print("Port Scan complete")
