# Set `$PATH` variable in Ubuntu

The `$PATH` variable is one of the default environment variable in linux (ubuntu). It is used by the shell to look for executable files or commands.

One way to permanently add a directory to `$PATH` environment variable is to use the `~/.profile` file. Add the following to the `~/.profile` file to add `myNewDir` to `$PATH`

```
$ export PATH=$PATH:/myNewDir
$ source ~/.profile
```

## The `source` command

`source` is a bash shell built-in command that executes the content of the file passed as argument, **in the current shell**. It has a synonym in `.` (period). 

Note that `./` and `source` are not quite the same: 

- `./script` runs the script as an executable file, launching a new shell to run it 
- `source some_script` reads and executes commands from filename in the current shell environment
- `source some_script` is the same as `. some_script`
