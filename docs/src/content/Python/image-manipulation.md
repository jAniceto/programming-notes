Title: Image manipulation in Python
Date: 2017-08-12 15:24
Authors: José Aniceto


The **Python Imaging Library** (PIL) development has stagnated, with its last release in 2009. Luckily, there’s an actively-developed fork of PIL called **Pillow**.
**Pillow** is easier to install, runs on all operating systems, and supports Python 3.

## Pillow

* Pillow and PIL cannot co-exist in the same environment. Before installing Pillow, please uninstall PIL.
* Pillow >= 2.0.0 supports Python versions 2.6, 2.7, 3.2, 3.3, 3.4
* Before installing Pillow, you’ll have to install Pillow’s prerequisites. [Instructions here](https://pillow.readthedocs.io/en/3.0.0/installation.html).

### Instalation:

**Windows**: 

`$ pip install Pillow`

**Linux (Debian or Ubuntu)**: 

Make sure you have Python’s development libraries installed. In Debian or Ubuntu: `$ sudo apt-get install python3-dev python3-setuptools`
Prerequisites are installed on Ubuntu 12.04 LTS or Raspian Wheezy 7.0 with: `$ sudo apt-get install libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk`

`$ pip install Pillow`

```python
from PIL import Image, ImageFilter
#Read image
im = Image.open( 'image.jpg' )
#Display image
im.show()

#Applying a filter to the image
im_sharp = im.filter( ImageFilter.SHARPEN )
#Saving the filtered image to a new file
im_sharp.save( 'image_sharpened.jpg', 'JPEG' )

#Splitting the image into its respective bands, i.e. Red, Green,
#and Blue for RGB
r,g,b = im_sharp.split()

#Viewing EXIF data embedded in image
exif_data = im._getexif()
exif_data
```
