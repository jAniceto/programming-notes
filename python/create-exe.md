# Create a standalone exacutable using `pyinstaller`

It's pretty straight forward:
1. Create an entry-point script that calls your main function.
2. Install PyInstaller.
3. Run PyInstaller on your entry-point.
4. Test your new executable.
5. Ship your resulting `dist/` folder to users.

## Install

To install `pyinstaller` on your pc run (more details can be found here: https://www.pyinstaller.org/):

```
pip install pyinstaller
```

## For a single file program

If your program is a single script use `cmd` to go to your program directory and to turn it into a exe folder run

```
pyinstaller myprogram.py
```


## For a package

Create an entrypoint outside your package folder that imports and runs your program. This will be the entry point. Call pyinstaller on the entrypoint script as above.

## Options

Change the name of your executable: 
```
pyinstaller myprogram.py --name MY_PROGRAM
```

Package your entire application into a single executable file: 
```
pyinstaller myprogram.py --onefile
```

Insert additional data or binary files into your build: 
```
pyinstaller myprogram.py --add-data data/file.csv
```

Exclude some modules from being included with your executable: 
```
pyinstaller myprogram.py --exclude-module=pytest
```

Avoid automatically opening a console window for stdout logging: 
```
pyinstaller myprogram.py -w
```


What I usually run: 

```
pyinstaller -F --windowed --icon=myapp.ico myprogram.py
```

This makes it a single exe (without the folders with all dependables) but is slightly slower, minimizes the console window sine I have a GUI, and gives it a snazzy icon that I had saved (you have to copy over the icon, or have an exception incase it isn't found)


## References

- [Using PyInstaller to Easily Distribute Python Applications](https://realpython.com/pyinstaller-python/)
