#location of ansible playbooks
location = '/opt/ans-between'
#host address local/127.0.0.1 for local or 0.0.0.0 for external use
host = '127.0.0.1'
#port to bind to
port = '8080'
#authtentication key for users(Not secure, looking at switiching to hashing)
auth = '123456' 
#default is gunicorn
server= 'gunicorn'

dbdir="/opt/ans-between/"

schemaloc="/opt/ans-between/"
