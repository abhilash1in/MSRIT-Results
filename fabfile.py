from fabric.api import local, settings, abort, run, cd, env

env.hosts = ['13.127.48.135']
env.user = 'ubuntu'
env.key_filename = '/Users/anirudh/Documents/Python-Projects/Results/key.pem'

def prepare_deploy(message='fab push'):
    local('git add -A && git commit'+" -m '"+message+"'")
    local('git push')

def deploy():
    code_dir = '/var/www/html/MSRIT-Results/'
    with cd(code_dir):
        run('sudo git pull')
        with cd(code_dir+'results'):
            run('sudo touch wsgi.py')
        
        
