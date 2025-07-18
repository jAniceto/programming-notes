# Ubuntu CLI cheat sheet

## System

### System information

`uname -a`: Displays all system information.

`hostnamectl`: Shows current hostname and related details.

`lscpu`: Lists CPU architecture information.

`timedatectl status`: Shows system time.


### System monitoring and management

`top`: Displays real-time system processes.

`htop`: An interactive process viewer (needs installation).

`df -h`: Shows disk usage in a human-readable format.

`free -m`: Displays free and used memory in MB.

`kill <process id>`: Terminates a process.


### Running commands

`<command> &`: Runs command in the background.

`jobs`: Displays background commands.

`fg <command number>`: Brings command to the foreground.


### Service management

`sudo systemctl start <service>`: Starts a service.

`sudo systemctl stop <service>`: Stops a service.

`sudo systemctl status <service>`: Checks the status of a service.

`sudo systemctl reload <service>`: Reloads a service’s configuration without `interrupting its operation.

`journalctl -f`: Follows the journal, showing new log messages in real time.

`journalctl -u <unit_name>`: Displays logs for a specific systemd unit.


### Cron jobs and scheduling

`crontab -e`: Edits cron jobs for the current user.

`crontab -l`: Lists cron jobs for the current user.


## Files

### File management

`ls`: Lists files and directories.

`touch <filename>`: Creates an empty file or updates the last accessed date.

`cp <source> <destination>`: Copies files from source to destination.

`mv <source> <destination>`: Moves files or renames them.

`rm <filename>`: Deletes a file.

### Directory navigation

`pwd`: Displays the current directory path.

`cd <directory>`: Changes the current directory.

`mkdir <dirname>`: Creates a new directory.

### File permissions and ownership

`chmod [who][+/-][permissions] <file>`: Changes file permissions.

`chmod u+x <file>`: Makes a file executable by its owner.

`chown [user]:[group] <file>`: Changes file owner and group.

### Searching and finding
`find [directory] -name <search_pattern>`: Finds files and directories.

`grep <search_pattern> <file>`: Searches for a pattern in files.

### Archiving and compression

`tar -czvf <name.tar.gz> [files]`: Compresses files into a tar.gz archive.

`tar -xvf <name.tar.[gz|bz|xz]> [destination]`: Extracts a compressed tar archive.

### Text editing and processing

`nano <file>`: Opens a file in the Nano text editor.

`cat <file>`: Displays the contents of a file.

`less <file>`: Displays the paginated content of a file.

`head <file>`: Shows the first few lines of a file.

`tail <file>`: Shows the last few lines of a file.

`awk ‘{print}’ <file>`: Prints every line in a file.
