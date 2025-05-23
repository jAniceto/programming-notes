# Create ReactJS app and deploy to Github pages

## Requirements
- **NodeJS** Install from [here](https://nodejs.org/en/). Check version with: `$ node --version`
- **npm** Check version with: `$ npm --version`

## Create React app

You can `npm` install `create-react-app` globally with: 
```
$ npm install -g create-react-app
$ create-react-app my-app
```

Alternatively, you can use `npx` (a tool to execute packages) to create the app withput installing `create-react-app`. This way is recommended by the docs.

```
$ npx create-react-app my-app
$ cd my-app
$ npm start
```

This will lunch a server where you can see your app.


## Deploying to Github Pages

### 1) Install the gh-pages package as a "dev-dependency" of the app
```
$ npm install gh-pages --save-dev
```

### 2) Create an empty repository on Github

Go to github.com and create a repo. We will name it named `react-gh-pages`. 

### 3) Modify the package.json file

At the top level, add a homepage property:
```
"homepage": "https://gitname.github.io/react-gh-pages"
```

In the existing scripts property, add the following:
```
"scripts": {
  //...
  "predeploy": "npm run build",
  "deploy": "gh-pages -d build"
}
```

### 4) Add the GitHub repository as a "remote" in your local git repository
```
$ git remote add origin https://github.com/gitname/react-gh-pages.git
```

### 5) Generate a production build of your app, and deploy it to GitHub Pages
```
$ npm run deploy
```

The app is now accessible at https://gitname.github.io/react-gh-pages/


### 6) Optionally, commit your source code to the "master" branch and push your commit to GitHub.
```
$ git add .
$ git commit -m "Create a React app and publish it to GitHub Pages"
$ git push origin master
```

So, the `master` branch helds the source code, and the `gh-pages` branch helds the built app code.


## References 

- [react-gh-pages](https://github.com/gitname/react-gh-pages)
- [Create React App](https://create-react-app.dev/docs/getting-started)
