Title: Linux Crontab
Date: 2017-09-07 10:44
Authors: José Aniceto
Modified: 2017-11-05 20:36

To view currently active crontab entries: `$ sudo crontab -l`

To enter the edit the crontab enter the following command in the terminal: `$ sudo crontab -e`

**Note:** Don't use `sudo` in a cron job. Instead edit root's crontab instead of your own, e.g. `sudo crontab -e` and then enter commands without `sudo`.

At the bottom of the file enter one line for each task in the following format:

``` 
Minute   Hour   Day of Month       Month          Day of Week        Command    
(0-59)  (0-23)     (1-31)    (1-12 or Jan-Dec)  (0-6 or Sun-Sat)               
```

The command must use a complete link. Instead of the first five fields, one of eight special strings may appear:

string        | meaning
---           | ---
@reboot       | Run once, at startup.
@yearly       | Run once a year, "0 0 1 1 *".
@annually     | (same as @yearly)
@monthly      | Run once a month, "0 0 1 * *".
@weekly       | Run once a week, "0 0 * * 0".
@daily        | Run once a day, "0 0 * * *".
@midnight     | (same as @daily)
@hourly       | Run once an hour, "0 * * * *".

#### Example 1: Run a python script every day a 16:15
```
15 16 * * * sudo python /home/pi/projects/script1.py
```

#### Example 2: Run a python script every five days a 18:30
```
30 18 */5 * * sudo python /home/pi/projects/script1.py
```


### Helpfull links:

https://crontab.guru
