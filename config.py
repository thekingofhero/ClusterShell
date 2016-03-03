def local_config():
	#master_address
	master_address = '172.18.0.40'
	#role:publisher /worker/collector
	role = 'worker'
	#port
	publish_port = 1234
	collector_port = 4321
	return locals()
