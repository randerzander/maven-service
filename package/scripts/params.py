#!/usr/bin/env python
from resource_management.libraries.functions.version import format_hdp_stack_version, compare_versions
from resource_management import *

# server configurations
config = Script.get_config()

package_dir = '/var/lib/ambari-agent/cache/stacks/HDP/2.2/services/r-stack'
resources_dir = package_dir + '/package/resources/'
scripts_dir = package_dir + '/package/scripts/'
