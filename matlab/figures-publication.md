# Preparing figures for publication

Here is a summary the most important steps and commands necessary to obtain nice figures of your data that can be imported into the text editing program of your choice.

## Scaling 

Here is how to set the figure dimensions to (8 x 6) cm:

```matlab
fig = figure;

% create figure here

fig.Units               = 'centimeters';
fig.Position(3)         = 8;
fig.Position(4)         = 6;
```

Alternatively, you can do the following and use the `gcf` command:

```matlab
set(gcf, 'units', 'centimeters', 'position', [0 0 width height])
```

The maximum width for one-column and two-column figures, respectively, is usually given by the journal you want to submit to. Or, if you are using a LaTeX, you can output the required widths with the `\the` command:

```latex
\the\hsize
```

## Formatting text

Here we select the font Times and set the font size to 9.

```matlab
set(fig.Children, ...
    'FontName',     'Times', ...
    'FontSize',     9);
```


## Remove unnecessary white space

As the white space surrounding the plot wastes a lot of the precious figure space, especially for small figures, it should be removed (or minimized) in the next step:

```matlab
set(gca, 'LooseInset', max(get(gca,'TightInset'), 0.02))
```


## Exporting

The figure can be exported to the desired graphics format. This can be done with the saveas command, but the print command allows for the definition of more attributes of the exported file. 

First, in order for the exported file to have the same size as the Matlab figure, it's necessary to first set the `PaperPositionMode` to automatic. Then we export the current figure to a png file with 600 dpi resolution:

```matlab
fig.PaperPositionMode   = 'auto';
print('img/my_figure', '-dpng', '-r600')
```

If using vector graphics, `-dpng` can be replaced by `-epsc` for colored eps.
