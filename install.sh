#!/usr/bin/env bash
set -e
PYTHONLOC="https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz"
GITLOC="https://github.com/bandit145/ans-between.git"
INSTALLLOC="/opt/ans-between"
#helper-functions
function venv_install(){
	cd /tmp
	pip3 install virtualenv
	virtualenv -p "/tmp/python3.5/bin/python3.5" "/opt/ans-between/venv"
	source /opt/ans-between/venv/bin/activate
	pip3 install -r $INSTALLLOC"/requirements.txt"
}
function create_account(){
	useradd ans-between
}
function create_log(){
	mkdir /var/log/ans-between
	chown ans-between:ans-between /var/log/ans-between
}

#does installing celery in venv work for system?
function place_configs(){
	cp /opt/ans-between/setup/ans-between /etc/init.d/
	cp /opt/ans-between/setup/celeryd /etc/init.d/
	cp /opt/ans-between/setup/celeryd.conf /wherever
	chmod +x /opt/etc/init.d/ans-between
	chmod +x /opt/etc/init.d/celeryd
}

function make_python(){
	cd /tmp
	if [ ! -e "/tmp/Python-3.5.2.tgz" ]; then
		wget $PYTHONLOC
	fi
	if [ ! -d "/tmp/Python-3.5.2" ]; then
		tar -xf "Python-3.5.2.tgz"
	fi
	cd "Python-3.5.2"
	./configure --prefix=/tmp/python3.5
	make
	make install
}


function git_clone(){
	if [ ! -d $INSTALLLOC ]; then 
		git clone $GITLOC $INSTALLLOC
	fi
}

git_clone
make_python
venv_install
place_configs
create_account
create_log