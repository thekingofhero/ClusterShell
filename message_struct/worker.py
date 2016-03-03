import zmq
import os
class worker:
	def __init__(self,):
		self.context = zmq.Context()
		self.reciever = self.context.socket(zmq.PULL)
		self.reciever.connect('tcp://localhost:5557')
		
		self.send_to_collector = self.context.socket(zmq.PUSH)
		self.send_to_collector.connect("tcp://localhost:5558")
	def recv(self,):	
		while True:
			s = self.reciever.recv()
			with os.popen(s) as fp:
				result = fp.read()
				self.send_to_collector.send(result)

if __name__ == '__main__':
	worker_obj = worker()
	worker_obj.recv()
