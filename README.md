An Ambari Stack service package for the Apache Maven java package build tool.

**Note:** Currently supports only RHEL/CentOS. Deploying this stack will automatically install the [EPEL Apache Maven](https://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo) repository if it isn't in /etc/yum.repos.d/ already.

To deploy, copy the entire directory into your Ambari stacks folder and restart Ambari:

```
git clone https://github.com/randerzander/maven-service
sudo mv maven-service /var/lib/ambari-server/resources/stacks/HDP/2.2/services/
sudo service ambari-server restart
```

Then you can click on 'Add Service' from the 'Actions' dropdown menu in the bottom left of the Ambari dashboard. When you've completed the install process, you will be able to use maven 'mvn' on all selected client nodes.

If you want to delete the Maven client from the Ambari services list (apache-maven will remain installed on selected nodes):
```
curl -u $user:$pass -i -H 'X-Requested-By: ambari' -X DELETE http://$host:8080/api/v1/clusters/$cluster/services/MAVEN
```
