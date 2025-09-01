# Create LaTeX presentations with Beamer

## Elements

### Columns

Create two columns:

```tex
\begin{columns}[T]
    \begin{column}{0.48\textwidth}
        % content
    \end{column}
    \begin{column}{0.48\textwidth}
        % content
    \end{column}
\end{columns}
```

This will leave `0.04\textwidth` of spacing between the columns. The `[T]` aligns the column content to the top. You can also use `c` for center and `b` for bottom.

### Blocks

Creating a block environment. 

```latex
\begin{block}{Block Title}
    % content
\end{block}

\begin{alertblock}{Block Title}
    % content
\end{alertblock}

\begin{exampleblock}{Block Title}
    % content
\end{exampleblock}
```


## Formating

Add vertical space between elements:

```latex
\vspace{0.5cm}
```

Font size:

```latex
\tiny This is tiny font size
\scriptsize This is scriptsize font size
\footnotesize This is footnotesize font size
\small This is small font size
\normalsize This is normalsize font size
\large This is large font size
\Large This is Large font size
\LARGE This is LARGE font size
\huge This is huge font size
\Huge This is Huge font size
```

## Templates

A good theme compilation can be found at: [The Ultimate Beamer Theme List](https://github.com/martinbjeldbak/ultimate-beamer-theme-list)

Here are a few select examples:

- [Metropolis](https://github.com/matze/mtheme)
- [Execushares](https://github.com/hamaluik/Beamer-Theme-Execushares)
- [wildcat](https://www.overleaf.com/latex/templates/wildcat/knynymwgrxxj)
- [ant-center-brief](https://www.overleaf.com/latex/templates/ant-center-brief/rhkgyzdnkhhn)
- [uic-presentation-template](https://www.overleaf.com/latex/templates/uic-presentation-template/dgjbtyvtgqcg)
