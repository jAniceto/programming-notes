# Sticky footer

Get the footer to stick to the bottom of the window even when there is not enough content to fill the page.

HTML:
```html
<body>
  <header>…</header>
  <main>…</main>
  <footer>…</footer>
</body>
```

CSS:
```css
body {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
}

main {
  flex: 1;
}
```

### References
- [https://philipwalton.github.io/solved-by-flexbox/demos/sticky-footer/](https://philipwalton.github.io/solved-by-flexbox/demos/sticky-footer/)

Other:
- [https://css-tricks.com/couple-takes-sticky-footer/](https://css-tricks.com/couple-takes-sticky-footer/)
- [https://getbootstrap.com/docs/4.0/examples/sticky-footer/](https://getbootstrap.com/docs/4.0/examples/sticky-footer/)
