# Web scrapping in Python
Web scrapping using Beautiful Soup and Requests


## Using Beautiful Soup 4 and Requests

Install:
```
$ pip install requests
$ pip install beautifulsoup4
```

Usage:
```python
import requests
from bs4 import BeautifulSoup

r = requests.get(card['url'])
soup = BeautifulSoup(r.content, "html.parser")
data = soup.find_all('span', attrs={'class': 'some_class'})
```
