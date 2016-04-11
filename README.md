# pindrop
Pindrop coding assessment.

Intall Pre-requisite:

1. Install psutil
   $ sudo apt-get install gcc python-dev
   $ pip install psutil

2. Install cherrypy
   $ sudo pip install cherrypy


Steps to run and API suppport:-

1. $ python pinLauncher.py
   this will start the cherrypy engine. To stop the cherry engine you can just press ctrl+c. Currently we are running in default setting of cherrypy. So it is launced at "http://127.0.0.1:8080/start"

2. To start the monitoring system either give curl request or from the browser go to :- http://127.0.0.1:8080/start
   -> This will start the monitoring service. 

3. To get the status of the machine use the following api:  http://127.0.0.1:8080/getstatus

4. To stop the monitoring system either give curl request or from the browser go to :- http://127.0.0.1:8080/stop
   -> This will stop the monitoring service.

Summary to run the program:
   1. python pinLauncher.py
   2. http://127.0.0.1:8080/start
   3. http://127.0.0.1:8080/getstatus
   4. http://127.0.0.1:8080/stop

Assumption:

1. Currently I am storing all the past records in 'system_stat.log' file. I would definitely use database schema like mysql and extend it with SQL ORM support by suing sqlobject. I am currently just appending the data to the log file but we can extend the capability of python inbuilt logging package and can have rotating file handler to have multiple files.

2. I will also have to handle the purging of past records in timely fashion. But due to limited time frame I could not add that support.

3. I am using cherryPy webframework to support the restFull API's.

