import zmq
import time
import threading
import sys
#from message_struct.collector import collector
from collector import collector
class publisher:
	def __init__(self,):
		self.context = zmq.Context()
		#sender
		self.sender = self.context.socket(zmq.PUSH)
		self.sender.bind('tcp://*:5557')
		#collector
		self.collector = collector()
		self.collector.start()

	def send(self,cmd):
		if cmd == 'q' or cmd == 'quit':
			self.collector.stop()
		self.sender.send(cmd)

if __name__ == '__main__':
	p = publisher()
	p.send('q')
