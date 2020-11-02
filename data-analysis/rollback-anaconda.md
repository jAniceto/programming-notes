# Rollback Anaconda environment

Sometimes updating your environment can bring unintended consequences. Fortunatly Anaconda allows you to list the changes to your environment and revert to a previous point.

List the history of each change to the current environment:

```
$ conda list --revisions
```

You'll get an output like this:

```
     ...
     
2020-06-24 12:47:58  (rev 12)
     _anaconda_depends  {2019.03 (defaults/win-64) -> 2020.02 (defaults/win-64)}
     astropy  {4.0 (defaults/win-64) -> 4.0.1.post1 (defaults/win-64)}
     atomicwrites  {1.3.0 (defaults/win-64) -> 1.4.0 (defaults/noarch)}
     autopep8  {1.4.4 (defaults/noarch) -> 1.5.3 (defaults/noarch)}
     backcall  {0.1.0 (defaults/win-64) -> 0.2.0 (defaults/noarch)}
     bcrypt  {3.1.7 (defaults/win-64) -> 3.1.7 (defaults/win-64)}
     beautifulsoup4  {4.8.2 (defaults/win-64) -> 4.9.1 (defaults/win-64)}
     bitarray  {1.2.1 (defaults/win-64) -> 1.2.2 (defaults/win-64)}
     ...
     xz  {5.2.4 (defaults/win-64) -> 5.2.5 (defaults/win-64)}
     yapf  {0.28.0 (defaults/noarch) -> 0.29.0 (defaults/noarch)}
     zipp  {2.2.0 (defaults/noarch) -> 3.1.0 (defaults/noarch)}
     zlib  {1.2.11 (defaults/win-64) -> 1.2.11 (defaults/win-64)}
     zstd  {1.3.7 (defaults/win-64) -> 1.4.4 (defaults/win-64)}
    -backports.os-0.1.1 (defaults/win-64)
    +brotlipy-0.7.0 (defaults/win-64)
    +importlib-metadata-1.6.1 (defaults/win-64)
    +prompt-toolkit-3.0.5 (defaults/noarch)
    +regex-2020.5.14 (defaults/win-64)
    +threadpoolctl-2.1.0 (defaults/noarch)
    +toml-0.10.1 (defaults/noarch)

2020-06-24 14:57:05  (rev 13)
    +plotly-4.8.1 (plotly/noarch)
    +retrying-1.3.3 (defaults/win-64)

2020-11-02 14:49:53  (rev 14)
     _anaconda_depends  {2020.02 (defaults/win-64) -> 2020.07 (defaults/win-64)}
     asn1crypto  {1.3.0 (defaults/win-64) -> 1.4.0 (defaults/noarch)}
     astroid  {2.3.3 (defaults/win-64) -> 2.4.2 (defaults/win-64)}
     astropy  {4.0.1.post1 (defaults/win-64) -> 4.0.2 (defaults/win-64)}
     attrs  {19.3.0 (defaults/noarch) -> 20.2.0 (defaults/noarch)}
     autopep8  {1.5.3 (defaults/noarch) -> 1.5.4 (defaults/noarch)}
     bcrypt  {3.1.7 (defaults/win-64) -> 3.2.0 (defaults/win-64)}
     ...
    +nest-asyncio-1.4.1 (defaults/noarch)
    +tifffile-2020.10.1 (defaults/win-64)
    +typed-ast-1.4.1 (defaults/win-64)
    +zope-1.0 (defaults/win-64)
    +zope.event-4.5.0 (defaults/win-64)
    +zope.interface-5.1.2 (defaults/win-64)
```

It list each revision along with updated packages (old version -> new version) and newly added packages (the ones with + symbol). Now you can safely rollback to previous versions of your environment by using `conda install -–revision revision number`. For instance:

```
conda install --revision 13
```
