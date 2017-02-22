# ans-between
NOTE: ans-between is still relatively untested

ans-between is a server that takes web requests with ansible commands in them and runs the ansible command, sorting its feedback for retreival.

##Setup
Configuring ans-between is fairly simple.(Soon to be simpler)

###Requirements
- python3
- ansible
- celery

###Setup
1. Download and put the files anywhere you wish.
2. Fill out the config.py file in the main ans-between directory /ans-between (or whatever you named it).
3. Copy or move the ans-between init.d script from the setup folder to /etc/init.d/
4. Create the directory /var/log/ans-between/
5. From the setup folder copy the celeryd init.d script into /etc/init.d/
6. From the setup folder copy the celeryd-conf file and place it into /etc/default/
7. start both as services and enjoy!

##Usage

######Communicating with ans-between
ans-between accepts json web requests, to submit a job you POST to "ipaddr"/job.
You will recieve a taskid, when you want to retrieve the output of that ansible run you GET to "ipaddr"/tasks/(taskid)

json job request:

{"name":'"taskname.yml","params":[{"-i":"192.167.8.9"},{"--extra-vars":"ayy"}],"args":["arg1","arg2"],"password":"testpass", "auth":"123456"}

This data all corresponds to the schema template discussed below, the one difference is the "auth" attribute. This is the password you set in the config.py file of ans-between to limit access to the program. 

######Entering schema data
The schema folder is where you create the templates for the ansible jobs, it supports python style commenting (#comment). You enter the template as a python dictionary:

- params: Typically named values that have two or more parts, for example -i 192.168.1.24 (ansible inventory cmd)
- args: Typically one off ansible "arguments"
- name: Name of the playbook

{'name':'taskname.yml','params':[{'-i':'inventory'},{'--extra-vars':'ayy'}],'args':['arg1','arg2'],'password':'sudo pass etc.'} (If you are passing a password to ans-between be sure celery logging is not set to debug and that you have configured ans-between behind an https proxy)

It is important to note that the schema entry does not need to contain the actual data as it is being submitted by user web request, the schema entry is just a bare bones template for basic data verification.
For example, here is my actual job submission:

{"name":"taskname.yml","params":[{"-i":"192.167.8.9"},{"--extra-vars":"something"}],"args":["-place","-thing"],"password":"testpass", "auth":"123456"} 
