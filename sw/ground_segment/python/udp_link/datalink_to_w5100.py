#!/usr/bin/python

<<<<<<< HEAD
from __future__ import print_function
=======
>>>>>>> 5926b573a907e168704d2426ee3d50a02e32d1b3
import os
import sys
import socket
import struct
from optparse import OptionParser

sys.path.append(os.getenv("PAPARAZZI_HOME") + "/sw/lib/python")

parser = OptionParser()
parser.add_option("-d", "--destip", dest="dest_addr", help="Destination IP for messages picked up from local socket", default="192.168.25.47")
parser.add_option("-p", "--destport", dest="dest_port", default=1234, help="Destination UDP port to send messages to")
parser.add_option("-l", "--localport", dest="local_port", default=4243, help="Local port to listen to for UDP messages")

(options, args) = parser.parse_args()

msock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
msock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
msock.bind(("", int(options.local_port)))
# mreq = struct.pack("4sl", socket.inet_aton(telemip), socket.INADDR_ANY)
# msock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# initialize a socket, think of it as a cable
# SOCK_DGRAM specifies that this is UDP
destsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

while( 1 ):
    data = None
    try:
      data, addr = msock.recvfrom(1024)

      format = 'B' * (len(data))
      strdata = struct.unpack( format, data )

<<<<<<< HEAD
      print(len( strdata ), ":", strdata)
=======
      print len( strdata ), ":", strdata
>>>>>>> 5926b573a907e168704d2426ee3d50a02e32d1b3

      # send the command
      destsock.sendto( data, (options.dest_addr, options.dest_port) )

<<<<<<< HEAD
    except socket.error as e:
      print('Exception', e)
=======
    except socket.error, e:
      print 'Exception', e
>>>>>>> 5926b573a907e168704d2426ee3d50a02e32d1b3

