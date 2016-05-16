#!/usr/bin/python
import socket
import sys
from socket import *
import logging
#from _codecs import decode
import thread

class ThreadedServer():

    serverSocket = socket(AF_INET, SOCK_STREAM)

    host = '127.0.0.1'
    port = int(sys.argv[1])
    serverSocket.bind((host,port))
    serverSocket.listen(5)


    print 'please send your http request to'+ str(host)+':'+ str(port)

    while True:
        
        print 'Ready to serve...'
        
        (client_connection, (client_ipaddress,client_port)) = serverSocket.accept()
        request = client_connection.recv(1024)
        print "Request:", request
        print "Client IP ADDRESS(Localhost):", client_ipaddress 
        print client_port
        request_method = request.split(' ')[0]
        print request_method
        #print socket.gethostname()
        try:
        
            if request_method == 'GET':
                print 'request method is GET'
                file_requested = request.split()
                file_requested = file_requested[1]
                print 'File_Requested:', file_requested
                if file_requested == '/HelloWorld.html':
                    exact_name = file_requested[1:]
                    file_handler = open(exact_name,'r')
                    response = file_handler.read().replace('\n','')
                    client_connection.send(response.encode('utf-8'))
                    client_connection.close()
        
                else:
                    response = '<html><body><p>Error 404: File not found</p><p>Python HTTP server</p></body></html>'
                    client_connection.send(response.encode('utf-8'))
                    client_connection.close()
       

      
        

        except Exception :
            logging.exception(" Exception occrusred")
    ThreadedServer().listen()

    serverSocket.close()     
