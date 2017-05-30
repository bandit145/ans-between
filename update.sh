#!/usr/bin/env bash
set -e
GITLOC="https://github.com/bandit145/ans-between.git"
INSTALLLOC="/opt/"

cd $INSTALLLOC"/opt/ans-between/"
git pull
pip install -U -r $INSTALLLOC"/ans-between/requirements.txt"
