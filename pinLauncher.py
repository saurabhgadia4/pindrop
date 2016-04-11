import cherrypy
import pinParam as Param
import pinStats as Stat
import threading
import time
import json

class APIHandler:
	def __init__(self):
		self.monitor = None

	@cherrypy.expose
	def index(self):
		return 'Welcome to cherry engine for monitoring system'

	@cherrypy.expose
	def start(self):
		self.monitor = Monitor()
		self.monitor.start_service()
		self.monitor.start()
		return 'Started Monitoring System'

	@cherrypy.expose
	def stop(self):
		self.monitor.stop_service()
		return 'Closed Monitoring System'

	def 


class Monitor(threading.Thread):
	def __init__(self, ):
		threading.Thread.__init__(self)
		self.log_file = Param.LOG_FILE_NAME
		self.__action = threading.Event()

	def start_service(self):
		self.__action.set()

	def stop_service(self):
		self.__action.clear()

	def run(self):
		print 'Service Started'
		count = 0
		while True:
			if not self.__action.isSet():
				break
			time.sleep(5)
			print count
			count+=1
		print 'exiting thread'
		

	def fetch_stat(self):
		data = Stat.Statistics.get_system_stat()
		json_data = json.dump(data, fobj)
		fobj.write('\n')



if __name__=="__main__":
	cherrypy.quickstart(APIHandler())

