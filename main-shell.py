import socket
import os
import sys
import time
import readline
from config import local_config
from message_struct.publisher import publisher
def main():
	publish = publisher()
	while True:
		try:
			cmd = raw_input('command:')
			publish.send(cmd)
			time.sleep(0.5)
			if cmd == 'q' or cmd == 'quit':
				break
		except:
			publish.send('q')
			break

if __name__ == '__main__':
	args = sys.argv
	main()
