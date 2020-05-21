# Profiling in Python

Python includes a profiler called [cProfile](https://docs.python.org/3/library/profile.html#module-cProfile). It not only gives the total running time, but also times each function separately, and tells you how many times each function was called, making it easy to determine where you should make optimizations.

You can call it from within your code, or from the interpreter, like this:

```python
import cProfile
cProfile.run('foo()')
```

Even more usefully, you can invoke the cProfile when running a script:

```python
python -m cProfile myscript.py
```

And I get this:
```
1007 function calls in 0.061 CPU seconds

Ordered by: standard name
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.061    0.061 <string>:1(<module>)
 1000    0.051    0.000    0.051    0.000 myscript.py:2(<lambda>)
    1    0.005    0.005    0.061    0.061 myscript.py:2(<module>)
    1    0.000    0.000    0.061    0.061 {execfile}
    1    0.002    0.002    0.053    0.053 {map}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler objects}
    1    0.000    0.000    0.000    0.000 {range}
    1    0.003    0.003    0.003    0.003 {sum}
```
