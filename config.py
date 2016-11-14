#host address local/127.0.0.1 for local or 0.0.0.0 for public
host = 'localhost'
#port to bind to
port = '8080'
#authtentication key for users(Not secure, looking at switiching to hashing)
auth = '123456' 
#default is gunicorn
server= 'gunicorn'
#workers
workers=4