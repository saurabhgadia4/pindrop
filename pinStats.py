import psutil
import time
import sys
import pinUtil as util

class Statistics:
	max_mem_usage = 0
	min_mem_usage = 100
	avg_mem_usage = 0
	max_disk_usage = 0
	max_cpu_usage = 0
	avg_cpu_usage = 0
	count=0

	def __init__(self):
		pass

	@classmethod
	def get_system_stat(cls):
		cls.count+=1
		data = {}
		data['cpu_stat'] = cls.get_cpu_details()
		data['memory_stat'] = cls.get_memory_details()
		data['disk_stat'] = cls.get_disk_details()
		return data

	@classmethod
	def get_cpu_details(cls):
		cpu_stat = {}
		cpu_stat['time_stat'] = cls.get_cpu_times()
		cpu_stat['usage'] = psutil.cpu_percent()
		cls.max_cpu_usage = max(cpu_stat['usage'],cls.max_cpu_usage)
		cls.avg_cpu_usage = (cls.avg_cpu_usage+cpu_stat['usage'])/cls.count
		return cpu_stat

	@classmethod
	def get_cpu_times(cls):
		time_dict = {}
		obj = psutil.cpu_times(percpu=False)
		time_dict['user'] = obj.user
		time_dict['system'] = obj.system
		time_dict['idle'] = obj.idle
		return time_dict

	@classmethod
	def get_memory_details(cls):
		memory_stat = {}
		memory_stat['vm'] = cls.get_virtual_mem_details()
		memory_stat['sm'] = cls.get_swap_mem_details()
		return memory_stat

	@classmethod
	def get_disk_details(cls):
		disk_stat = {}
		disk_stat['part_stats'] = cls.get_disk_partition_stats()
	
		disk_stat['count_stats'] = cls.get_disk_counters()
		return disk_stat

	@classmethod
	def get_virtual_mem_details(cls):
		vm_obj = psutil.virtual_memory()
		vm = {}
		vm['total'] = vm_obj.total
		vm['used'] = vm_obj.used
		vm['free'] = vm_obj.free
		vm['percent'] = vm_obj.percent
		cls.max_mem_usage = max(vm['percent'], cls.max_mem_usage)
		cls.min_mem_usage = min(vm['percent'], cls.min_mem_usage)
		cls.avg_mem_usage = (cls.avg_mem_usage+vm['percent'])/cls.count
		vm['active'] = vm_obj.active
		vm['inactive'] = vm_obj.inactive
		return vm

	@classmethod
	def get_swap_mem_details(cls):
		sm = {}
		sm_obj = psutil.swap_memory()
		sm['total'] = sm_obj.total
		sm['used'] = sm_obj.used
		sm['free'] = sm_obj.free
		sm['percent'] = sm_obj.percent
		return sm

	@classmethod
	def get_disk_counters(cls):
		count_dict = {}
		counter = psutil.disk_io_counters(perdisk=False)
		count_dict['read_count'] = counter.read_count
		count_dict['write_count'] = counter.write_count
		count_dict['read_bytes'] = counter.read_bytes
		count_dict['write_bytes'] = counter.write_bytes
		return count_dict

	@classmethod
	def get_disk_partition_stats(cls):
		partition_stats = []
		use = 0
		cnt = 0
		for partition in psutil.disk_partitions(all=False):
			data = {}
			cnt+=1
			data['device'] = partition.device
			data['mt_pt'] = partition.mountpoint
			usage = psutil.disk_usage(data['mt_pt'])
			data['used_mem'] = usage.used
			data['total_mem'] = usage.total
			data['free_mem'] = usage.free
			data['used_percent'] = int(usage.percent)
			use=(use+data['used_percent'])/cnt
			partition_stats.append(data)
		cls.max_disk_usage = max(cls.max_disk_usage,use)
		return partition_stats

	