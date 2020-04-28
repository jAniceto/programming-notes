# React

React is a declarative, efficient, and flexible JavaScript library for building user interfaces. It lets you compose complex UIs from small and isolated pieces of code called "components".


## Index
- [Setup](#setup)
- [Project structure](#project-structure)
- [References](#references)


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


## Project structure

There is no recommended way to structure React projects. The simplest way is to create a components folder to store all component files, however the most common approaches rely on grouping files by features or routes, or grouping by file type.

Components folder:
```
src/
    components/
      Avatar.js
      Avatar.css
      Feed.js
      Feed.css
      FeedStory.js
      FeedStory.test.js
      Profile.js
      ProfileHeader.js
      ProfileHeader.css
```

Grouping by features or routes:
```
src/
    common/
      Avatar.js
      Avatar.css
      APIUtils.js
      APIUtils.test.js
    feed/
      index.js
      Feed.js
      Feed.css
      FeedStory.js
      FeedStory.test.js
      FeedAPI.js
    profile/
      index.js
      Profile.js
      ProfileHeader.js
      ProfileHeader.css
      ProfileAPI.js
```

Grouping by file type:
```
src/
    api/
      APIUtils.js
      APIUtils.test.js
      ProfileAPI.js
      UserAPI.js
    components/
      Avatar.js
      Avatar.css
      Feed.js
      Feed.css
      FeedStory.js
      FeedStory.test.js
      Profile.js
      ProfileHeader.js
      ProfileHeader.css
```

For instance, an utilities folder can be placed as:
```
src/
    components/
    utils/
        utilFunctions.js
```

Make sure to export functions like this:
```
export function func1() {

}

export function func2() {

}
```

Then import them like so:
```
import { func1, func2 } from './utils'
```


## References
- [React folder structure](https://www.robinwieruch.de/react-folder-structure)
- [React Docs on file structure](https://reactjs.org/docs/faq-structure.html)
- [React boilerplate example](https://github.com/react-boilerplate/react-boilerplate/tree/master/app)
