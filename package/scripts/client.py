import sys, os
from resource_management import *

class Client(Script):
  def install(self, env):
    self.configure(env)

    # Install EPEL repo for mono-devel
    if not os.path.exists('/etc/yum.repos.d/epel-apache-maven.repo'):
      Execute('cp '+params.resources_dir+'epel-apache-maven.repo /etc/yum.repos.d/')
    self.install_packages(env)

  def configure(self, env):
    import params
    env.set_params(params)

  def status(self, env): raise ClientComponentHasNoStatus()

if __name__ == "__main__":
  Client().execute()
