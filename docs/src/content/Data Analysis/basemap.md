Title: Geo ploting with Basemap
Date: 2019-12-18 14:09
Authors: José Aniceto


The matplotlib basemap toolkit is a library for plotting 2D data on maps in Python.

## Basemap installation

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
