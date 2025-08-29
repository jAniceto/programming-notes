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


## Templates

A good theme compilation can be found at: [The Ultimate Beamer Theme List](https://github.com/martinbjeldbak/ultimate-beamer-theme-list)

Here are a few select examples:

- [Metropolis](https://github.com/matze/mtheme)
- [Execushares](https://github.com/hamaluik/Beamer-Theme-Execushares)
- [wildcat](https://www.overleaf.com/latex/templates/wildcat/knynymwgrxxj)
- [ant-center-brief](https://www.overleaf.com/latex/templates/ant-center-brief/rhkgyzdnkhhn)
- [uic-presentation-template](https://www.overleaf.com/latex/templates/uic-presentation-template/dgjbtyvtgqcg)
