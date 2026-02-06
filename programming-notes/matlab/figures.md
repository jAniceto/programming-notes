# Figures in MATLAB

Hierarchy of Figure objects.

<img width="399" height="290" alt="v2_gobjects_top-01" src="https://github.com/user-attachments/assets/ef906218-3256-4932-a98e-2091c0b706b3" />



## Commonly usefull plot options

Take the following example:

```matlab
plot(x, y, '-', DisplayName='blabla', HandleVisibility='off')
```

 - `DisplayName`: Label for the data. Calling `legend()` will create thee legend using the `DisplayName`.
 - `HandleVisibility`: If `off` the series will not appear in the legend.



## Reset color order

```matlab
set(gca,'ColorOrderIndex',1)  % reset color order for plot
```

or

```matlab
ax = gca;
ax.ColorOrderIndex = 1;  % reset color order for plot
```
