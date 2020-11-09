# Set expiration time (TTL) for LocalStorage

It's not possible to specify expiration for items saved to a browser LocalStorage. However, we can use Javascript to add a TTL (Time To Live) to invalidate items in localStorage after a certain period of time elapses.

## Storing items with expiration time

Set a key in localStorage, and store the expiration time along with it:

```javascript
function setWithExpiry(key, value, ttl) {
	const now = new Date()

	// item is an object which contains the original value as well as the time when it's supposed to expire
	const item = {
		value: value,
		expiry: now.getTime() + ttl,
	}
	localStorage.setItem(key, JSON.stringify(item))
}
```

## Storing items with expiration time

Verify the expiration time while retrieving items from localStorage:

```javascript
function getWithExpiry(key) {
	const itemStr = localStorage.getItem(key)
	// if the item doesn't exist, return null
	if (!itemStr) {
		return null
	}
	const item = JSON.parse(itemStr)
	const now = new Date()
	// compare the expiry time of the item with the current time
	if (now.getTime() > item.expiry) {
		// If the item is expired, delete the item from storage and return null
		localStorage.removeItem(key)
		return null
	}
	return item.value
}
```

## References 

- [How to Set Expiry Time (TTL) for LocalStorage With Javascript](https://www.sohamkamani.com/blog/javascript-localstorage-with-ttl-expiry/)
