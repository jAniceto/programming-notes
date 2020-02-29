# React

React is a declarative, efficient, and flexible JavaScript library for building user interfaces. It lets you compose complex UIs from small and isolated pieces of code called "components".

## Setup

Best way to set up React is via NodeJS package manager `npm`. Go to [nodejs.org](https://nodejs.org/) and download NodeJS (LTS version is recommended). It is also recommended to install [React Developer Tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi)

To start a project we use the `create-react-app` tool. By using `npx` we run the `create-react-app` script without installing. Using `npm` will install the `create-react-app` package globally.

```bash
mkdir my-app
npx create-react-app .
npm start
```

This creates the following project structure:

```
my-app
├── README.md
├── node_modules
├── package.json           <-- app info and dependencies
├── .gitignore
├── public
│   ├── favicon.ico
│   ├── index.html         <-- main webpage where React is outputed
│   └── manifest.json
└── src
    ├── App.css
    ├── App.js             <-- App component
    ├── App.test.js
    ├── index.css
    ├── index.js           <-- React entry point
    ├── logo.svg
    └── serviceWorker.js
 ```
