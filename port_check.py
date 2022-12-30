#!/usr/bin/env python3
# sector 31 port check utility
# Author: AuxGrep

import socket
import sys

try:
  internal_port = int(sys.argv[1])

  def check_port_sector31():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)                                      
    result = sock.connect_ex(('127.0.0.1', internal_port)) #dont change anything here
  
    if result == 0:
      print ('Congraturations your port \033[1;33m{0}\033[0m is OPENED! ready to G0!.....\033[0;32m[ 0K ]\033[0m'.format(internal_port))

    else:
      print ('\033[0;31mport {0} is CLOSED try to open it\033[0m'.format(internal_port))
      sys.exit()

  check_port_sector31();

except:
  sys.exit()
