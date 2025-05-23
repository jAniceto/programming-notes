# Scientific quality figures

## 1) Using `SciencePlots`

[SciencePlots](https://github.com/garrettj403/SciencePlots/) is a Python pakage that provides Matplotlib styles for scientific figures. Install with:

```
$ pip install SciencePlots
```

To use, simple add the import and select the style:

```python
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')
```

To use any of the styles temporarily, you can use a constext manager:

```python
with plt.style.context('science'):
    plt.figure()
    plt.plot(x, y)
    plt.show()
```

More information and available styles can be found [here](https://github.com/garrettj403/SciencePlots/).


## 2) Using a predifined stylesheet

You can create and install a custom Matplotlib style. Install the styles by copying the respective `*.mplstyle` file into your Matplotlib style directory. To check where this is, in an interactive python console type:

```python
import matplotlib
print(matplotlib.get_configdir())
```

You should get back something like `/home/johndoe/.matplotlib`. You can then put the `*.mplstyle` file in `/home/johndoe/.matplotlib/stylelib/` (you may need to create the stylelib directory). Here is a base configuration for a scientific style:

```mplstyle
# Matplotlib style for scientific plotting
# Base style

# Set color cycle: blue, green, yellow, red, violet, gray
axes.prop_cycle : cycler('color', ['0C5DA5', '00B945', 'FF9500', 'FF2C00', '845B97', '474747', '9e9e9e'])

# Set default figure size
figure.figsize : 3.5, 2.625

# Set x axis
xtick.direction : in
xtick.major.size : 3
xtick.major.width : 0.5
xtick.minor.size : 1.5
xtick.minor.width : 0.5
xtick.minor.visible : True
#xtick.top : True

# Set y axis
ytick.direction : in
ytick.major.size : 3
ytick.major.width : 0.5
ytick.minor.size : 1.5
ytick.minor.width : 0.5
ytick.minor.visible : True
#ytick.right : True

# Set line widths
axes.linewidth : 0.5
grid.linewidth : 0.5
lines.linewidth : 1.

# Remove legend frame
legend.frameon : False

# Always save as 'tight'
savefig.bbox : tight
savefig.pad_inches : 0.05

# Use serif fonts
font.serif : cmr10, Computer Modern Serif, DejaVu Serif
font.family : serif
axes.formatter.use_mathtext : True
mathtext.fontset : cm

# Use LaTeX for math formatting
text.usetex : True
text.latex.preamble : \usepackage{amsmath} \usepackage{amssymb}
```

You can then use the styles in a similar fashion to that shown above. The following will apply the style globally:

```python
plt.style.use('science')
```

You can also combine multiple styles by:

```python
plt.style.use(['science', 'grid'])
```

To use styles on a figure by figure basis, use a contect manager:

```python
with plt.style.context('science'):
    plt.figure()
    plt.plot(x, y)
    plt.show()
```

More styles [here](https://gist.github.com/jAniceto/e58cf2738b970de54910d886d91093ee).


## 3) Additional usefull formating


```python
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText

with plt.style.context('science'):
    fig, ax = plt.subplots()
    
    ax = plot(x, y)

    # Labels
    ax.set_xlabel(r'$D_{12}$ $\mathrm{(cm^2 s^{-1})}$')  # x-axis label using LaTeX
    ax.set_ylabel(r'Y axis label')  # y-axis label using LaTeX

    # Ticks and grids
    ax.grid(False)  # Remove grid
    ax.set_xlim([1, 11])  # Set x-axis limits
    ax.set_ylim([6.5, 8.5])  # Set y-axis limits
    
    ax.ticklabel_format(style='sci', axis='x', scilimits=(0,0))  # Set x-axis ticks to scientific notation
    ax.ticklabel_format(style='sci', axis='both', scilimits=(0,0))  # Set both axis ticks to scientific notation

    # Add a text box to a corner of the graph with e.g. 'a)'
    anchor_text = AnchoredText('a)', pad=0, loc='upper right', frameon=False, prop=dict(fontweight="bold", fontsize=12, fontfamily='serif'))
    ax.add_artist(anchor_text)

    plt.tight_layout()

    fig.set_size_inches(5.25, 3.95)  # Set figure size in inches

    fig.savefig('fig1.png', dpi=300, bbox_inches='tight')  # Save figure in png
    fig.savefig('fig1.pdf', dpi=300, bbox_inches='tight')  # Save figure in pdf
```

