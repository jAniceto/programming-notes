# Derivatives

The [`esdiff`](https://ctan.org/pkg/esdiff?lang=en) package has handy macros for derivatives and partial derivatives, taking care of indices.

```latex
\documentclass{article}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{mathtools}
\usepackage[thinc]{esdiff}

\begin{document}

  First order derivative: df/dx

  \begin{equation}
      \diff{f}{x}
  \end{equation}

  Fourth order derivative: d4f/dx4|x=1

  \begin{equation}
      \diff*[4]{f}{x}{x = 1}
  \end{equation}

  First order partial derivative:

  \begin{equation}
      \diffp{f}{x}
  \end{equation}

  Second order crossed partial derivative

  \begin{equation}
    \diffp{g}{tu}
  \end{equation}

\end{document}
```


## References:

- [Is there a short hand command to write derivatives?](https://tex.stackexchange.com/questions/412439/is-there-a-short-hand-command-to-write-derivatives)
