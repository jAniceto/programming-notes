# Simple CSS reset

```css
html {
  box-sizing: border-box;
  font-size: 16px;
}

*, *:before, *:after {
  box-sizing: inherit;
}

body, h1, h2, h3, h4, h5, h6, p, ol, ul {
  margin: 0;
  padding: 0;
  font-weight: normal;
}

img {
  max-width: 100%;
  height: auto;
}
```

The CSS above will:

- Reset is the `box-sizing: border-box`, as this will ensure consistent and predictable sizing. The default value of content-box doesn't account for the padding or border. This is probably the most important point.

- Dont' bold headings by default with `font-weight: normal`.

- Set the default font size to be 16px. Everything else can be specified in rem units and it will be based on those 16px. Then, if you want to adjust globally to make the text a little larger overall, you can change the base rule for something like 17 or 18px.

- Make images responsive by default.
