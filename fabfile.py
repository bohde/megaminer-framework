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
    env.hosts = env.hosts[0:1]

def echo():
    run('uname -a')
    
def deploy():
    rsync_project('/tmp/')

def run_redirect():
    cd('megaminer/server/')
    run('screen python2.6 main.py --redirect', pty=True)  

def run_server():
    cd('megaminer/server/')
    run('screen python2.6 main.py --address %s' % env.hosts[0], pty=True)
