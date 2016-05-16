#!/usr/bin/python
import socket
import time
import sys
import logging
import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = sys.argv[1]
port = int(sys.argv[2])
file_requested = sys.argv[3]


try :
        request=" "
        start_time=time.time()
        clientSocket.connect((host, port))

        t= "GET " 
        t2=" /HTTP/1.0\n\n"
        RequestFinal=t+file_requested+t2
        #print start_time
        clientSocket.send(RequestFinal)
        while True:
                resp = clientSocket.recv(1024)
                if resp == "": break
                print resp

        end_time=time.time()
        total_time=((end_time)-(start_time))
        print "RTT in seconds:",total_time

except Exception():
        logging.exception(" Exception occrusred")
        # Close the connection when completed
clientSocket.close()
print "\ndone"

print (" Server HostName:")
print(socket.gethostname())
#print (" Server peername:")
print ("Server socket address info-> Hostname,aliaslist,ipaddrlist")
print (socket.gethostbyaddr(host))
print ("Server TimeOut:")
print (socket.getdefaulttimeout())
print ("Socket type (SOCK_STREAM):")
print (socket.SOCK_STREAM)
print ("Server Socket Address family(AF_INET):")
print (socket.AF_INET)
print ("Socket type (SOCK_STREAM):")
print (socket.SOCK_STREAM)
print ("Server Socket Family:IPPROTO_TCP")
print (socket.IPPROTO_TCP)

