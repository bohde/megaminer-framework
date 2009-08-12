import getpass
from fabric.api import env, run, local, cd, put
from fabric.contrib.project import rsync_project

env.project='megaminer4'

def _gen_hosts():
    env.hosts = ['rc%02ixcs213.managed.mst.edu' % x for x in xrange(1,9)]
    env.user = raw_input('Username: ')

def live():
    """Set hosts to the campus linux boxes"""
    _gen_hosts()
    env.password = getpass.getpass()
  
def master():
    """Set hosts to the first campus linux box"""
    _gen_hosts()
    env.hosts = env.hosts[:1]

def echo():
    run('uname -a')
    
def deploy():
    rsync_project('~')
