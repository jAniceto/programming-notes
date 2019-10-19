Title: Web scrapping with Beautiful Soup 4 
Date: 2017-11-09 13:27
Authors: José Aniceto
Modified: 2017-11-28 14:16

## Required modules
```
pip install beautifulsoup4
pip install lxml
pip instal html5lib
pip install requests
```

## Usage

```python
from bs4 import BeautifulSoup
import requests

source = requests.get('http://example.com').text
soup = BeautifulSoup(source, 'lxml')
```

## References

https://www.youtube.com/watch?v=ng2o98k983k
