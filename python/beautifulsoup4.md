# Web scrapping with Beautiful Soup 4 

## Required modules
```
pip install beautifulsoup4
pip install lxml
pip instal html5lib
pip install requests
```

## Usage

```
from bs4 import BeautifulSoup
import requests

source = requests.get('http://example.com').text
soup = BeautifulSoup(source, 'lxml')
```

## References

https://www.youtube.com/watch?v=ng2o98k983k
