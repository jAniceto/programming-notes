# Integrating from data points

Consider the following data

```matlab
t = [ ... ];
y = [ ... ];
```

## Matlab trapz function
Calculate the area (integral) directly from the datapoints.

```matlab
int_trapz = trapz(t,y)
```

## Fiting a curve to data and then integrating

```matlab
[fitobject,gof,output] = fit(t,y,'cubicspline');
```

### Calculate with Matlab integrate function from the fitted curve

```matlab
int_fit_integrate = integrate(fitobject, t(end), 0)
```

### Calculate with simpson38 function from the fitted curve

```matlab
int_fit_simp38 = simpson38(fitobject, 0, t(end), 3*100)
```


## Simpson's 3/8 rule

```matlab
%% 
function integral = simpson38(f , a , b , n)
%{
description:
    this function evaluates the integral of a mathematical function f
    between the limits a and b using the simpson's 1/3 formula given by,
        I = 3 * h / 8 * (f(a) + f(b) + 3 * f(x_interiors))
    
inputs:
    1. f = the function which to be integrated.
    2. a = lower limit of the integral.
    3. b = upper limit of the integral.
    4. n = the no of intervals to which the domain is to be split. note
    that n is always even for this case.
    note: n is an optional argument. if n is not specified, the function
    splits the interval into 60 pieces.
outputs:
    1. integral = this will give the value of the integral of the
    mathematical function f between the limits a and b.
%}
    %adding robustness - argumental pre-check
    if nargin < 3
        error('not enough input arguments. minimum 3 arguments needed.')
    end
    
    if a > b
        error("lowerlimit can't be greater than upperlimit.")
    end
    
    if mod(n , 3) ~= 0
        error("n must be a multiple of 3.")
    end
    
    if nargin < 4
        n = 60;
    end
        
    %calculate h value
    h = (b - a) / n;
    
    %evaluate the function values
    x = linspace(a , b , n + 1);
    for i = 1 : n + 1
       fofx(i) = f(x(i)); 
    end
 
    %split up the points
    g = fofx;
    g(1) = [];
    g(end) = [];
    inot3 = 0; %not a 3 multiple
    i3 = 0; %is a 3 multiple
    
    global g_3;
    for j = 1 : length(g)
        if mod(j , 3) == 0
            i3 = i3 + 1;
            g_3(i3) = g(j);
        else
            inot3 = inot3 + 1;
            g_not3(inot3) = g(j);
        end
    end
    
    if isempty(g_3)
        g_3 = 0;
    end
    
    %evaluate the integral
    integral = 3 * h / 8 * (fofx(1) + fofx(end) + 3 * sum(g_not3) + 2 * sum(g_3));
   
end
```


## Composite Simpson's 3/8 rule

```matlab
function int = simpson38comp(f, a, b, n)

if nargin < 3
    error('Not enough input arguments.')
end

if a > b
    error("Lower limit can't be greater than upper limit.")
end

if mod(n , 3) ~= 0
    error("n must be a multiple of 3.")
end

h=(b-a)/n;

so = 0;
sm3 = 0;

% (3h/8)*[(y0+yn)+2*(y3+y6+..+yn-3)+3*(y1+y2+y4+y5+...+yn-2+yn-1)]
for k = 1:1:n-1
    x(k) = a+k*h;
    y(k) = f(x(k));
    
    if rem(k,3) == 0
       sm3 = sm3+y(k);  %sum of multiple of 3 terms 
    else
        so = so+y(k);  %sum of others terms 
    end
end

int = (3*h/8)*(f(a)+f(b)+3*so+2*sm3);
```
