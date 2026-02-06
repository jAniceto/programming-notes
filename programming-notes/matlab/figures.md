# Figures in MATLAB

Hierarchy of Figure objects.

<img width="399" height="290" alt="v2_gobjects_top-01" src="https://github.com/user-attachments/assets/ef906218-3256-4932-a98e-2091c0b706b3" />



## Reset color order

```matlab
set(gca,'ColorOrderIndex',1)  % reset color order for plot
```

or

```matlab
ax = gca;
ax.ColorOrderIndex = 1;  % reset color order for plot
```
