Title: Keep SSH sessions running after disconnecting
Date: 2017-09-07 10:44
Authors: José Aniceto


### Using nohup

```
$ nohup long-running-process &
$ exit
```

### Using GNU Screen

```
$ screen             # to start a screen session
$ run-a-process
CTRL+a , d           # to detatch from your screen session
$ exit               # to disconnect from the server, while run-a-process continues
$ screen -r          # to resume the screen session when you come back to your laptop
```

### Using tmux
```
$ tmux               # to start a screen session
$ run-a-process
Ctrl+b then d        # to detatch from your session
$ tmux attach        # to resume the session when you come back to your laptop
```
