# Create artificial data

Sometimes we want to create artificial (synthetic) data so that we can use it in an example of in a test. For instance, imagine we have a script that fits a function to data and we want to test it on some data. We can generate that data artificially.

## General approach

```matlab
% Define the range of x values
x = linspace(0, 10, 100);

% Define the true function (e.g., a quadratic)
y_true = 2*x.^2 + 3*x + 5;

% Add some random noise to simulate measurement errors
noise = randn(size(x)) * 10;  % Gaussian noise with std dev = 10
y_noisy = y_true + noise;

% Plot the noisy data
figure;
plot(x, y_noisy, 'o');
hold on;
plot(x, y_true, '-');
legend('Noisy Data', 'Function');
xlabel('x');
ylabel('y');
```

## Types of noise

The most common noise types you can add include Gaussian (normal), uniform, and Poisson.

### Gaussian noise

Simulates measurement errors or natural variation in physical systems.

```matlab
x = linspace(0, 10, 100);

y_true = 2*x.^2 + 3*x + 5;  % function

sigma = 10;  % standard deviation of noise
noise = randn(size(x)) * sigma;
y_noisy = y_true + noise;
```

Using `randn` gives standard normal values (mean 0 and standard deviation 1). `sigma` controls the intensity of the noise.


### Uniform Noise

Every value within a range is equally likely. This is less realistic, but can be useful.

```matlab
range = 5;  % total range of uniform noise
noise = (rand(size(x)) - 0.5) * range;
y_noisy = y_true + noise;
```

Using `rand` generates values between [0, 1], we can then shift and scale to get the desired range.


### Poisson Noise

Useful for count data.

```matlab
y_true = 20 * exp(-0.5*x);   % expected count values
y_noisy = poissrnd(y_true);  % Poisson-distributed noise
```
The `poissrnd` function takes the expected (mean) value for each x. The output is directly a Poisson-distributed version of the expected value. It requires the Statistics and Machine Learning Toolbox.
