import cherrypy
import pinParam as Param
import pinStats as Stat
import threading
import time
import json
import datetime

class APIHandler:
	def __init__(self):
		self.monitor = None

	@cherrypy.expose
	def index(self):
		return 'Welcome to cherry engine for monitoring system'

	@cherrypy.expose
	def start(self):
		if self.monitor==None:
			self.monitor = Monitor()
			self.monitor.start_service()
			self.monitor.start()
			return 'Started Monitoring System'
		else:
			return 'Monitoring Service has already started'

	@cherrypy.expose
	def stop(self):
		if self.monitor:
			self.monitor.stop_service()
			self.monitor = None
			return 'Closed Monitoring System'
		else:
			return 'Monitoring system is already stopped'

	@cherrypy.expose
	def get_stats(self):
		stats = {}
		if not self.monitor:
			return 'Please start the monitoring service'
		return self.monitor.get_statistics()


class Monitor(threading.Thread):
	last_service_started = None
	last_service_stop = None

	def __init__(self, time_step=Param.TIME_STEP):
		threading.Thread.__init__(self)
		self.log_file = Param.LOG_FILE_NAME
		self.__action = threading.Event()
		self.time_step = time_step
		self.wobj = None
		self.robj = None
		self.cpu_stat_overall = {}
		self.memory_stat_overall = {}
		self.disk_stat_overall = {}
		self.lock = threading.Lock()
		self.__init()

	def __init(self):
		self.wobj = open(self.log_file, 'a')
		self.robj = open(self.log_file, 'r')
		self.last_service_started = str(datetime.datetime.today())

	def start_service(self):
		self.__action.set()

	def stop_service(self):
		self.__action.clear()
		self.last_service_stop = str(datetime.datetime.today())

	def run(self):
		print 'Service Started'
		count = 0
		while True:
			time.sleep(self.time_step)
			if not self.__action.isSet():
				self.wobj.close()
				self.robj.close()
				break
			self.lock.acquire()
			data = self.__fetch_current_stat()
			self.lock.release()
		print 'Exiting Monitoring Thread'
		

	def __fetch_current_stat(self):
		data = Stat.Statistics.get_system_stat()
		data['time'] = time.time()
		json_data = json.dump(data, self.wobj)
		self.wobj.write('\n')
		self.wobj.flush()
		return data

	def __fetch_agg_stat(self):
		data = {}
		data['service_start_time'] = self.last_service_started
		data['avg_mem_usage'] = str(Stat.Statistics.avg_mem_usage)+'%'
		data['max_mem_usage'] = str(Stat.Statistics.max_mem_usage)+'%'
		data['min_mem_usage'] = str(Stat.Statistics.min_mem_usage)+'%'
		data['max_disk_usage'] = str(Stat.Statistics.max_disk_usage)+'%'
		data['max_cpu_usage'] = str(Stat.Statistics.max_cpu_usage)+'%'
		data['avg_cpu_usage'] = str(Stat.Statistics.avg_cpu_usage)+'%'
		return data

	def get_statistics(self):
		self.lock.acquire()
		curr_data = self.__fetch_current_stat()
		agg_data = self.__fetch_agg_stat()
		self.lock.release()
		data = {}
		data['current_stat'] = curr_data
		data['past_stat'] = agg_data
		return json.dumps(data)



if __name__=="__main__":
	cherrypy.quickstart(APIHandler())

