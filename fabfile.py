# -*- coding: utf-8 -*-

from fabric.api import local
from fabric.api import env
# from fabric.api import settings
from fabric.api import run
from fabric.api import cd

env.hosts = ["spacelive.club"]
env.user = 'vincent'


def deploy():
    local("mkdir -p /tmp/build")
    local("tar -jcvf /tmp/build/spacelive.tar.bz2 ./*")
    local("scp /tmp/build/spacelive.tar.bz2 vincent@spacelive.club:/tmp")
    run("mkdir -p /home/vincent/spacelive")
    code_dir = '/home/vincent/spacelive'
    # run("pip install git+https://github.com/wisonwang/pyweb.git")
    with cd(code_dir):
        run("rm -rf *;cp /tmp/spacelive.tar.bz2 .; tar -axvf spacelive.tar.bz2")
        run("supervisorctl start spacelive")