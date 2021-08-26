# Design of Experiments

**Note: Requires Matlab Statistics Toolbox.**

The Statistics Toolbox offers a collection of DOE tools rather than a beginning-to-end DOE application. Here's how to use some of those tools. 

You can generate a full factorial design for four factors each taking two values as follows:
```matlab
design = fullfact([2 2 2 2])
```

For historical reasons, this codes the two levels as 1 and 2. The fracfact function codes them as -1 and 1. Here's how to use that function to get the equivalent design and its confounding pattern:
```matlab
[design,confounding] = fracfact('a b c d')
```

Here's how to generate a 2^(4-1) design:
```matlab
[design,confounding] = fracfact('a b c abc')
```

Here's how to change the limits in the first column to other limits that you specify (you could repeat for other columns or loop over them):
```matlab
limits = [5 10];
design(:,1) = limits(1) + (limits(2)-limits(1))*(1+design(:,1))/2
```

Finally, you may want to randomize the order of runs when you carry out the experiment. Here's how to do that:
```matlab
order = randperm(8)
design = design(order,:)
```
