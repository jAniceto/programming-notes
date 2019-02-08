# Basic Javascript concepts

## Variables 

There are three main keywords used to define variables in JavaScript:
- `const`: defines a constant variable that cannot be redefined later
- `let`: defines a variable is local to the scope of the innermost pair of curly braces surrounding it
- `var`: defines a variable that is local to the function it is defined in

Here is an example showcasing these different ways to define variables:

```javascript
// This variable exists even outside the loop
if (true) {
    var message = 'Hello!';
}

alert(message);
```

Because `var` was used to define message, there will be no errors running this code.

```javascript
// This variable does not exist outside the loop
if (true) {
    let message = 'Hello!';
}

alert(message);
```

Because `let` was used to define message, it cannot be passed to alert, which is outside the scope of message. If this were in an HTML page, when the page was opened, no alert would pop up. If the console were opened in the browser, there would be an `Uncaught ReferenceError`.

```javascript
// The value of const variables cannot change
const message = 'Hello!';
message = 'Goodbye!';

alert(message);
```
  
Similar to the last example, no alert will pop up. In the console, there would be an `Uncaught TypeError`, since there was an attempt to redefine a variable defined with `const`.

## Template literals (formating strings)

```javascript
const name = 'Daniel';
alert(`Hello ${name}!`);
```

                  
