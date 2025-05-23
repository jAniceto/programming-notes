# Deploying to Github pages with `ghp-import`

## Example directory structure

```
myproject/
├── myproject/
├── jupyterbook/
├── README.md
├── requirements.txt
├── build.bat
```

## Building with `ghp-import`

The build.bat file can then be used to run:

```batch
jupyter-book build jupyterbook
cd jupyterbook
ghp-import -n -p -f _build/html
cd ..
```


## References

- [GitHub Pages Import](https://github.com/c-w/ghp-import)
