Title: Hiding Passwords and Secret Keys in Environment Variables
Date: 2018-02-02 13:31
Authors: José Aniceto


### Adding a Environment Variable (Windows)

System Menu > `Advanced System Settings` > `Environment Variables...` > in User Variables click `New...` > insert variable name (VAR_NAME) and value (VAR_VALUE)

When coding it may be necessary to restart your IDE or text editor.

### Adding a Environment Variable (Linux and Mac)

Open the terminal:

```
$ cd 
$ nano .bash_profile
```

To the file add the line and save:
```
export VAR_NAME="VAR_VALUE"
```

When coding it may be necessary to restart your IDE or text editor.

### Acessing your Environment Variables in Python

```python
import os

var1 = os.environ.get('VAR_NAME')
```
