#
#       PEDA - Python Exploit Development Assistance for GDB (python3 version)
#
#       Copyright (C) 2012 Long Le Dinh <longld at vnsecurity.net>
#       Copyright (C) 2014 Jeffrey Crowell <crowell at bu.edu>
#
#       License: see LICENSE file for details
#
from __future__ import print_function
import random
import socket
import struct
try:
    import http.client as httplib
except:
    import httplib

from codecs import encode, decode
from utils import msg, error_msg

class Payload():
	"""
    Simple wrapper for payload generation
    """
    def __init__(self, arch="x86", platform="linux"):
    	pass