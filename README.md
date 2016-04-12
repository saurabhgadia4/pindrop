# pindrop
Pindrop coding assessment.

Python Version:'2.7.6 (default, Jun 22 2015, 17:58:13) \n[GCC 4.8.2]'
Intall Pre-requisite packages:

1. Install psutil
   $ sudo apt-get install gcc python-dev
   $ pip install psutil

2. Install cherrypy
   $ sudo pip install cherrypy


Steps to run monitor service and API suppport:-

1. $ python pinLauncher.py
   this will start the cherrypy engine. To stop the cherry engine you can just press ctrl+c. Currently we are running in default setting of cherrypy. So it is launced at "http://127.0.0.1:8080/start"

2. To start the monitoring system either give curl request or from the browser go to :- http://127.0.0.1:8080/start
   -> This will start the monitoring service. 

3. To get the status of the machine use the following api:  http://127.0.0.1:8080/get_stats

This API returns the current systems status and past aggregate system status. Following is the sample result given by this api call:
{
"current_stat": 
	-> "memory_stat": 
		-> "vm": {"used": 2580987904, "percent": 18.0, "free": 5704212480, "inactive": 742002688, "active": 1664167936, "total": 
				  8285200384}, 
		-> "sm": {"total": 4000313344, "percent": 0.0, "free": 4000313344, "used": 0}}, 
	-> "time": 1460421017.382492, 
	-> "disk_stat": 
		-> "count_stats": {"write_bytes": 1100665856, "read_count": 21075, "read_bytes": 689047040, "write_count": 38773}, 
		-> "part_stats": [{"used_percent": 5, "free_mem": 238802780160, "total_mem": 265467244544, "used_mem": 13155872768, "mt_pt": " 
							/", "device": "/dev/sda8"}, {"used_percent": 5, "free_mem": 490102784, "total_mem": 520093696, "used_mem": 
							29990912, "mt_pt":"/boot/efi", "device": "/dev/sda1"}, {"used_percent": 19, "free_mem": 168882507776, "total_
							mem": 209715195904, "used_mem": 40832688128, "mt_pt": "/media/saurabh/Office", "device": "/dev/sda4"}]}, 
	-> "cpu_stat": {"usage": 13.4, "time_stat": {"idle": 90185.2, "user": 2498.32, "system": 526.52}}},

"past_stat": {"max_cpu_usage": "13.4%", "max_disk_usage": "8%", "avg_mem_usage": "2.63838293651%", "service_start_time": "2016-04-11 
				17:30:10.976343", "min_mem_usage": "17.9%", "avg_cpu_usage": "1.80828869048%", "max_mem_usage": "18.0%"}
}

4. To stop the monitoring system either give curl request or from the browser go to :- http://127.0.0.1:8080/stop
   -> This will stop the monitoring service.

Summary to run the program:
   1. python pinLauncher.py
   2. http://127.0.0.1:8080/start
   3. http://127.0.0.1:8080/get_stats
   4. http://127.0.0.1:8080/stop

Assumption:

1. Currently I am storing all the past records in 'system_stat.log' file. I would definitely use database schema like mysql and extend it with SQL ORM support by suing sqlobject. I am currently just appending the data to the log file but we can extend the capability of python inbuilt logging package and can have rotating file handler to have multiple files.

2. I will also have to handle the purging of past records in timely fashion. But due to limited time frame I could not add that support.

3. I am using cherryPy webframework to support the restFull API's.

4. I have also not added any exception handling code. Provided time I can add specific exception handling code where ever required.

