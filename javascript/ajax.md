# Making AJAX request

## Send a Request To a Server (Pure Javascript)

```javascript
// Create a new XMLHttpRequest
var request = new XMLHttpRequest();

// Handle state changes for the request.
request.onreadystatechange = function() {
  if (request.readyState == 4 && request.status == 200) {
    // Do something like:
    var jsonData = JSON.parse(request.responseText);
  }
};

// Set up and make the request
request.open("GET", "ajax_info.txt", true);
request.send();
```

Where:

* `open(method, url, async)`: Specifies the type of request. *method*: the type of request: GET or POST; *url*: the server (file) location; *async*: true (asynchronous) or false (synchronous)

* `send()`: Sends the request to the server (used for GET)

* `send(string)`: Sends the request to the server (used for POST). For instance: `xhttp.send("fname=Henry&lname=Ford");`

* `onreadystatechange`: defines a function to be executed when the request receives an answer
