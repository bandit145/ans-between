#location of ansible playbooks
location = '/home/phil/'
#host address local/127.0.0.1 for local or 0.0.0.0 for external use
host = '127.0.0.1'
#port to bind to
port = '8080'
#authtentication key for users(Not secure, looking at switiching to hashing)
auth = '123456' 
#default is gunicorn
server= 'gunicorn'
#workers
workers=4

dbdir="/home/phil/git/ans-between/"

schemaloc="/home/phil/git/ans-between/"