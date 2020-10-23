# Bibliography management

## Using `bibtext` (default)

```latex
\bibliographystyle{stylename}
\bibliography{bibfile}
```

Where `bibfile` is the name of the bibliography .bib file, without the extension, and `stylename` is the bibliography style. A simple numeric style is `unsrt`


## Using `biblatext` package

`biblatext` is the most complete and flexible bibliography tool in the LaTeX world.

```latex
\documentclass[12pt]{article}

\usepackage[backend=biber,style=numeric,sorting=ynt]{biblatex}
\addbibresource{journals.bib,phd-references.bib}

\begin{document}

\cite{robertson2007}
\cite{earnshaw1842}

\printbibliography

\end{document}
```

Where journals.bib and phd-references.bib are BibTeX databases

## The bibliography database file (`.bib`)

```bibtex
@article{einstein,
    author =       "Albert Einstein",
    title =        "{Zur Elektrodynamik bewegter K{\"o}rper}. ({German})
    [{On} the electrodynamics of moving bodies]",
    journal =      "Annalen der Physik",
    volume =       "322",
    number =       "10",
    pages =        "891--921",
    year =         "1905",
    DOI =          "http://dx.doi.org/10.1002/andp.19053221004",
    keywords =     "physics"
}

@book{dirac,
    title={The Principles of Quantum Mechanics},
    author={Paul Adrien Maurice Dirac},
    isbn={9780198520115},
    series={International series of monographs on physics},
    year={1981},
    publisher={Clarendon Press},
    keywords = {physics}
}

@online{knuthwebsite,
    author    = "Donald Knuth",
    title     = "Knuth: Computers and Typesetting",
    url       = "http://www-cs-faculty.stanford.edu/~uno/abcde.html",
    keywords  = "latex,knuth"
}

@inbook{knuth-fa,
    author = "Donald E. Knuth",
    title = "Fundamental Algorithms",
    publisher = "Addison-Wesley",
    year = "1973",
    chapter = "1.2",
    keywords  = "knuth,programming"
}
...
```

## References

- [Bibtex bibliography styles - Overleaf](https://www.overleaf.com/learn/latex/bibtex_bibliography_styles)
- [Bibliography management with biblatex - Overleaf](https://www.overleaf.com/learn/latex/Bibliography_management_with_biblatex)
