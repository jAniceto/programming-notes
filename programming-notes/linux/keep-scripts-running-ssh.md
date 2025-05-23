# Keep processes running and closing SSH connection

The are several alternatives. Here we cover `nohup` and `tmux`.

## Using `nohup`

```
$ nohup long-running-command &
```
It logs `stdout` to `nohup.log`.


## Using `tmux`

1) SSH into the remote machine.

2) Install `tmux`:
```
$ apt install tmux
```

3) Start `tmux`:
```
$ tmux
```

4) Start the process you want inside the started `tmux` session.

5) Leave/detach the `tmux` session by typing `Ctrl+b` and then `d`.

6) You can now safely log off from the remote machine, your process will keep running inside `tmux`.

7) When you come back again and want to check the status of your process you can attach to your tmux session using:
```
$ tmux attach
```

If you want to have multiple sessions running side-by-side, you should name each session using `Ctrl+b` and `$`. 

You can get a list of the currently running sessions using:
```
$ tmux list-sessions
```
or 
```
$ tmux ls
```

To attach to a running session with use:
```
$ tmux attach-session -t <session-name>
```
