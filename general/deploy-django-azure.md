# Deploy Django app to Azure App Service

## Run a cronjob in Azure App Service (Linux)

SSH into the container and copy the current startup script by typing the following:

```
$ cp /opt/startup/startup.sh /home
```

Edit the `startup.sh` under `/home/startup.sh` and add your changes to the top of the file after `#!/bin/sh`. In the sample below, I'll be installing cron to run a cronjob.

```sh
# Installing cron
apt-get update -qq && apt-get install cron -yqq
service cron start
mkdir /home/BackupLogs
(crontab -l 2>/dev/null; echo "*/5 * * * * cp /home/LogFiles/*.log /home/BackupLogs")|crontab
```

Save the file.

In the Azure Portal configurations, add `/home/startup.sh` as the Startup Command and restart the site.

![](https://i.stack.imgur.com/WMuGX.png)

Note, there are two pitfalls to this approach:
- The script must be executable, so either install w/ unix and chmod 755 start.sh or use a git command (see SO).
- The 3pp (here crontab) is installed on every startup, thus you depend on external servers/repositories when starting the webapp.


References for this section:

- https://stackoverflow.com/questions/57654279/how-to-run-cronjobs-on-an-azure-linux-hosted-webapp
- https://azureossd.github.io/2020/01/23/custom-startup-for-nodejs-python/index.html


## References

- [Deploying a Django App to Azure App Service](https://testdriven.io/blog/django-azure-app-service/)
- [Deploy a Python (Django or Flask) web app with PostgreSQL in Azure](https://learn.microsoft.com/en-us/azure/app-service/tutorial-python-postgresql-app?tabs=django%2Cwindows)
