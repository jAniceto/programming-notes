Title: Geo ploting with Basemap
Date: 2019-12-18 14:09
Authors: José Aniceto


The matplotlib basemap toolkit is a library for plotting 2D data on maps in Python.

## Installation

#### Option 1:

The recommended installation method for Basemap is using Anaconda and the conda-forge channel. In the Anaconda Prompt run:
```
$ conda install -c anaconda basemap
```

You might also need to run the following command to install [PROJ](https://proj.org/install.html), which is a required dependency of Basemap:
```
$ conda install -c conda-forge proj
```

If the installation was sucessful you should now be able to run the following import in the Python (Anaconda) prompt without any errors:
```python
from mpl_toolkits.basemap import Basemap
```

#### Option 2:

If you are on Windows you can also install the binaries directly. This worked better for me than installing through Anaconda and conda-forge. Download the [Basemap](https://www.lfd.uci.edu/~gohlke/pythonlibs/#basemap) and [PROJ](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyproj) binaries. Make sure you download the correct binary for your Python version. For instance, if you have Python 3.7 64-bit make sure to download the `pyproj‑2.4.2.post1‑cp37‑cp37m‑win_amd64.whl` and `basemap‑1.2.1‑cp37‑cp37m‑win_amd64.whl` files. The `cp37` indicates Python version and `amd64` the 64-bit version. You can now install both libraries with pip.

```
$ pip install pyproj‑2.4.2.post1‑cp37‑cp37m‑win_amd64.whl
$ pip install basemap‑1.2.1‑cp37‑cp37m‑win_amd64.whl
```

Test the instalation by running:

```python
from mpl_toolkits.basemap import Basemap
```


## Ploting a simple map

Let's plot a simple world map.

```python
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

m = Basemap(projection='mill',llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')

# Draw map features
m.drawcoastlines()
m.fillcontinents(color='#072B57',lake_color='#FFFFFF')

# Draw parallels and meridians
m.drawparallels(np.arange(-90.,91.,30.))
m.drawmeridians(np.arange(-180.,181.,60.))

m.drawmapboundary(fill_color='#FFFFFF')
plt.title("Basemap Example!")
plt.show()
```

`projection='mill'` is the map projection. There are multiple projections availlable. Check [here](https://matplotlib.org/basemap/users/mapsetup.html).

`llcrnrlat`, `llcrnrlon`, `urcrnrlat`, and `urcrnrlon` are the latitude and longitude values of the lower left and upper right corners of the map.

There are three resolution levels: `resolution='c'` (used above) is crude resolution but faster render time. There is also `resolution='l'` for low resolution and `resolution='h'` for high resolution, which represent increasing map resolution and increased render time. Unless coastlines or lakes are really important to you crude resolution is usually enough.


## Drawing other map features:

```python
m.drawcountries()  # draw countries
m.drawstates()  # draw states
m.drawrivers()  # draw rivers
m.bluemarble()  # satellite style map
```


## Ploting coordinates

```python
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='mill',llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')
m.drawcoastlines()
m.fillcontinents(color='#072B57',lake_color='#FFFFFF')
m.drawmapboundary(fill_color='#FFFFFF')

lat, lon = 29.7630, -95.3630  # define the coordinates
x,y = m(lon, lat)  # convert to Basemap system using your map
m.plot(x, y, 'ro', markersize=20, alpha=.5)  # plot and specify marker size and marker fill transparency

plt.title("Basemap Example!")
plt.show()
```




## References:
- [Basemap installation via Anaconda](https://anaconda.org/anaconda/basemap)
- [PROJ installation instructions](https://proj.org/install.html)
- [pythonprogramming.net](https://pythonprogramming.net/geographical-plotting-basemap-tutorial/)
