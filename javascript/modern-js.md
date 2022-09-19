# Modern JavaScript

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

## String interpolation (string literals)

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



