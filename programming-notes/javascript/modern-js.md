# Modern JavaScript

Index:
  * [Imports and exports](#imports-and-exports)
  * [Variables](#variables)
  * [Equality and inequality comparisons](#equality-and-inequality-comparisons)
  * [String interpolation](#string-interpolation)
  * [For-Of loops](#for-of-loops)
  * [Arrow Functions](#arrow-functions)
  * [Promises](#promises)
  * [Async and await](#async-and-await)
  * [Spread operator](#spread-operator)
  * [Classes](#classes)
  * [Reference](#reference)

## Imports and exports 

With modern JavaScript front end frameworks, applications can now use a dependency model that is based on imports and exports. A JavaScript module that wants to make a function or variable available for other modules to use, can declare it as a default export. Let's say there is a `cool.js` module with `myCoolFunction()` inside. Here is how this module could be written:

```javascript
export default function myCoolFunction() {
  console.log('this is cool!');
}
```

Any other module that wants to use the function can then import it:

```javascript
import myCoolFunction from './cool';
```

In this import, `./cool` is the path of the dependent module, relative to the location of the importing file. The path can navigate up or down the directory hierarchy as necessary. The `.js` extension can be included in the import filename, but it is optional.

When using default exports, the name of the exported symbol does not really matter. The importing module can use any name it likes. The next example is also valid:

```javascript
import myReallyCoolFunction from './cool';
```

Importing from third-party libraries works similarly, but the import location uses the library name instead of a local path. For example, here is how to import the `React` object:

```javascript
import React from 'react';
```

A module can have only one default export, but it can also export additional things. Here is an extension of the above `cool.js` module with a couple of exported constants:

```javascript
export const PI = 3.14;
export const SQRT2 = 1.41;

export default function myCoolFunction() {
  console.log('this is cool!');
}
```

To import a non-default export, the imported symbol must be enclosed in `{` and `}` braces:

```javascript
import { SQRT2 } from './cool';
```

This syntax also allows multiple imports in the same line:

```javascript
import { SQRT2, PI } from './cool';
```

Default and non-default symbols can also be included together in a single import line:

```javascript
import myCoolFunction, { SQRT2, PI } from './cool';
```

## Variables

Starting with ES6, the `let` and `const` keywords are used for the declaration of variables and constants respectively.

```javascript
let a;
let a = 1;
```

A constant is a variable that can only be assigned a value when it is declared:

```javascript
const c = 3;
console.log(c); // 3
c = 4;  // error
```

## Equality and inequality comparisons

In general, all equality and inequality comparisons should use the newer operators. Examples:

```javascript
let a = 1;

console.log(a === 1);  // true
console.log(a === '1');  // false
console.log(a !== '1');  // true
```

## String interpolation

```javascript
const name = 'susan';
let greeting = `Hello, ${name}!`;  // "Hello, susan!"
```

## For-Of loops

Older versions of JavaScript only provide strange and contorted ways to iterate over an array of elements, but luckily ES6 introduces the `for ... of` statement for this purpose.

Given an array, a for-loop that iterates over its elements can be constructed as follows:

```javascript
const allTheNames = ['susan', 'john', 'alice'];
for (name of allTheNames) {
  console.log(name);
}
```

## Arrow Functions
ES6 introduces an alternative syntax for the definition of functions that is more concise, in addition to having a more consistent behavior for the this variable, compared to the function keyword.

Consider the following function, defined in the traditional way:

```javascript
function mult(x, y) {
  const result = x * y;
  return result;
}

mult(2, 3);  // 6
```

Using the newer arrow function syntax, the function can be written as follows:

```javascript
const mult = (x, y) => {
  const result = x * y;
  return result;
};

mult(2, 3);  // 6
```

Looking at this it isn't very clear why the arrow syntax is better, but this syntax can be simplified in a few ways. If the function has a single statement instead of two, then the curly braces and the return keyword can be omitted, and the entire function can be written in a single line:

```javascript
const mult = (x, y) => x * y;
```

If the function accepts a single argument instead of two, then the parenthesis can also be omitted:

```
const square = x => x * x;

square(2);  // 4
```

When passing a callback function as an argument to another function, the arrow function syntax is more convenient. Consider the following example, shown with traditional and arrow function definitions:

```javascript
longTask(function (result) { console.log(result); });

longTask(result => console.log(result));
```

## Promises

A promise is a proxy object that is returned to the caller of an asynchronous operation running in the background. This object can be used by the caller to keep track of the background task and obtain a result from it when it completes.

The promise object has `then()` and `catch()` methods (among others) that allow the construction of chains of asynchronous operations with solid error handling.

Many internal and third-party JavaScript libraries return promises. Here is an example use of the `fetch()` function to make an HTTP request, and then print the status code of the response:

```javascript
fetch('https://example.com').then(r => console.log(r.status));
```

This executes the HTTP request in the background. When the fetch operation completes, the arrow function passed as an argument to the `then()` method is invoked with the response object as an argument.

Promises can be chained. A common case that requires chaining is when making an HTTP request that returns a response with some data. The following example shows how the request operation is chained to a second background operation that reads and parses JSON data from the server response:

```javascript
fetch('http://example.com/data.json')
  .then(r => r.json())
  .then(data => console.log(data));
```
  
This is still a single statement, but I have broken it up into multiple lines to increase clarity. Once the `fetch()` call completes, the callback function passed to the first `then()` executes with the response object as an argument. This callback function returns `r.json()`, a method of the response object that also returns a promise. The second `then()` call is invoked when the second promise completes, receiving the parsed JSON data as an argument.

To handle errors, the catch() method can be added to the chain:

```javascript
fetch('http://example.com/data.json')
  .then(r => r.json())
  .then(data => console.log(data))
  .catch(error => console.log(`Error: ${error}`));
```

## Async and await

Promises are a nice improvement that help simplify the handling of asynchronous operations, but having to chain several actions in long sequences of `then()` calls can still generate code that is difficult to read and maintain.

In the 2017 revision of ECMAScript, the async and await keywords were introduced as an alternative way to work with promises. Here is the first `fetch()` example from the previous section once again:

```javascript
fetch('http://example.com/data.json')
  .then(r => r.json())
  .then(data => console.log(data));
```

Using async/await syntax, this can be coded as follows:

```javascript
async function f() {
  const r = await fetch('https://example.com/data.json');
  const data = await r.json();
  console.log(data);
}
```

With this syntax, the asynchronous tasks can be given sequentially, and the resulting code looks very close to how it would be with synchronous function calls. A limitation is that the `await` keyword can only be used inside functions declared with `async`.

Error handling in async functions can be implemented with try/catch:

```javascript
async function f() {
  try {
    const r = await fetch('https://example.com/data.json');
    const data = await r.json();
    console.log(data);
  }
  catch (error) {
    console.log(`Error: ${error}`);
  }
}
```

An interesting feature of functions declared as `async` is that they are automatically upgraded to return a promise. The `f()` function above can be chained to additional asynchronous tasks using the `then()` method if desired:

```javascript
f().then(() => console.log('done!'));
```

Or of course, it can also be awaited if the calling function is also `async`:

```javascript
async function g() {
  await f();
  console.log('done!');
}
```

The arrow function syntax can also be used with `async` functions:

```javascript
const g = async () => {
  await f();
  console.log('done!');
};
```

## Spread operator

The spread operator (`...`) can be used to expand an array or object in place. 

```javascript
const a = [5, 3, 9, 2, 7];
console.log(Math.min(...a));  // 2
```

The basic idea is that the `...a` expression expands the contents of `a`, so the `Math.min()` function receives five independent arguments instead of single array argument.

The spread operator can also be used to create a new array by mixing another array with new elements:

```javascript
const a = [5, 3, 9, 2, 7];
const b = [10, ...a, 8, 0];  // [10, 5, 3, 9, 2, 7, 8, 0]
```
It also allows for a simple way to do a shallow copy of an array:

```javascript
const c = [...a];  // [5, 3, 9, 2, 7]
```
The spread syntax also works with objects:

```javascript
const d = {name: 'susan'};
const e = {...d, age: 20};  // {name: 'susan', age: 20}
const f = {...d};  // {name: 'susan'}
```

An interesting usage of the spread operator on objects is to make partial updates:

```javascript
const user = {name: 'susan', age: 20};
const new_user = {...user, age: 21};  // {name: 'susan', age: 21}
```

Here, the collision that occurs when having two values for the age key is resolved by using the version that appears last.


## Classes

A big omission in the earlier versions of the JavaScript language up to, and including ES5 is classes, which are the core component of object-oriented programming. Below you can see an example of an ES6-style class:

```javascript
class User {
  constructor(name, age, active) {  // constructor
    this.name = name;
    this.age = age;
    this.active = active;
  }

  isActive() {  // standard method
    return this.active;
  }

  async read() {  // async method
    const r = await fetch(`https://example.org/user/${this.name}`);
    const data = await r.json();
    return data;
  }
}
```

To create an instance of a class, the new keyword is used:

```javascript
const user = new User('susan', 20, true);
```

## Reference

[The React Mega-Tutorial by Miguel Grinberg](https://blog.miguelgrinberg.com/post/introducing-the-react-mega-tutorial)
