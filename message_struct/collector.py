import zmq
import threading
import sys

class collector(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.thread_stop = False
		self.context = zmq.Context()
		self.collect_all = self.context.socket(zmq.PULL)
		self.collect_all.bind("tcp://*:5558")

	def run(self):
		while not self.thread_stop:
			self.collect()
		print('STOP')
	
	def collect(self):
		s = self.collect_all.recv()
		sys.stdout.write(s)

	def stop(self):
		self.thread_stop = True
