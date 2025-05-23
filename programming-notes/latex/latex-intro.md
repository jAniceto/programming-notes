# An Introduction to LaTeX

## Managing large documents

For smaller projects it is okay to keep everything in a single `.tex` file. For more involved projects this approach quickly becomes cumbersome. The `\include` command makes it possible to break your document down into smaller chunks. Working with smaller chunks is more manageable. An example structure for a thesis project could look like the following:

```
thesis/
|-- thesis.tex
|-- chapters/
    |-- chapter_1.tex
    |-- chapter_2.tex
    |-- chapter_3.tex
|-- internal/
    |-- preamble.tex
|-- fig/
    |-- science.png
|-- references.bib
```

Example `thesis.tex`:

```latex
\documentclass[12pt]{report}

\include{internal/preamble}

\begin{document}

\include{chapters/chapter _1}
\include{chapters/chapter _2}
\include{chapters/chapter _3}

\bibliography{references}

\end{document}
```

Example `internal/preamble.tex`:

```latex
% Preamble, packages, commands, etc .
\ usepackage{microtype}
\ usepackage{booktabs}
\ usepackage{cleveref}
\ usepackage{graphicx}

% Make it easier to include figures
\graphicspath{{fig/}}
```

Example `chapters/chapter_1.tex`:

```python
\chapter{Literature review}
\label{cha:lit _ review}

Here's stuff others did which I don't really understand \ldots
```

## Custom commands

### Simple macros

Used to simplify repetitive and/or complex formatting. Usually specified in the preamble:

```latex
\newcommand{\name}{definition}
```

### Macros with parameters

```latex
\newcommand{\name}[#params]{definition}
```

For example: 

```latex
\newcommand{\bb}[1]{\mathbb{#1}}
```


### Macros with default parameters

```latex
\newcommand{\name}[# params][default #1]{def.}
```

For example: 

```latex
\newcommand{\plusbinomial}[3][2]{(#2 + #3)^#1}
```

## References

- [Preparing your thesis with LaTeX](https://jwalton.info/assets/teaching/latex/slides.pdf)
- [Thesis based on Tufte style](http://www.ccs.neu.edu/home/turon/thesis.pdf)
- [ClassicThesis – A “classically styled” thesis package](https://ctan.org/pkg/classicthesis?lang=en)
- [Entry types which BibTeX understands](https://bib-it.sourceforge.net/help/fieldsAndEntryTypes.php#Entries)
- [Plot publication-quality figures with matplotlib and LaTeX](https://jwalton.info/Embed-Publication-Matplotlib-Latex/)
