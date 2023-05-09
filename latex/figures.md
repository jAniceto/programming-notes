# Working with figures

## Simple figure

```latex
\begin{figure}[!htbp]
    \centering
    \includegraphics{path/to/figure.pdf}
    \caption{Figure caption here.}
    \label{fig:fig-label}
\end{figure}
```

The `!htbp` forces the image position.


## Figures side by side

```latex
\usepackage{graphicx}
\usepackage{caption}
\usepackage{subcaption}


\begin{figure}
    \centering
    \begin{subfigure}{0.45\textwidth}
        \includegraphics{fig1.pdf}
        \label{fig:fig1}
        \caption{fig1 caption}
    \end{subfigure}
    
    \begin{subfigure}{0.45\textwidth}
        \centering
        \includegraphics{fig2.pdf}
        \label{fig:fig2}
        \caption{fig2 caption}
    \end{subfigure}
    \caption{global caption}
\end{figure}
```
