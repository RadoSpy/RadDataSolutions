import socket

if socket.gethostname()=='LAPTOP-QI6FKBFV':
	from .local_settings import *
else:
	from .prod_settings import *