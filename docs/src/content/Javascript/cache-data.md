Title: Caching data
Date: 2017-12-03 11:50
Authors: José Aniceto


You have three options:

1. Cookies: https://developer.mozilla.org/en-US/docs/DOM/document.cookie
2. DOMStorage (sessionStorage or localStorage): https://developer.mozilla.org/en-US/docs/DOM/Storage
3. If your users are logged in, you could persist data in your server's DB that is keyed to a user (or group)


### Using localStorage (persistent over sessions)

Writing :
```javascript
localStorage['myKey'] = 'somestring'; // only strings
```

Reading :
```javascript
var myVar = localStorage['myKey'] || 'defaultValue';
```

If you need to store complex structures, you might serialize them in JSON. For example :

Reading :
```javascript
var stored = localStorage['myKey'];
if (stored) myVar = JSON.parse(stored);
else myVar = {a:'test', b: [1, 2, 3]};
```

Writing :
```javascript
localStorage['myKey'] = JSON.stringify(myVar);
```

Note that you may use more than one key. They'll all be retrieved by all pages on the same domain.

Unless you want to be compatible with IE7, you have no reason to use the obsolete and small cookies.


### References
https://stackoverflow.com/questions/14266730/js-how-to-cache-a-variable
