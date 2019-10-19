Title: Seaborn
Date: 2019-10-19 12:08
Authors: José Aniceto


## Change overal asthetics

Scaling plot elements, like line widths. In increasing size:

```python
sns.set_context("paper")
sns.set_context("notebook")  # default
sns.set_context("talk")
sns.set_context("poster")
```

Scaling overall text size:

```python
sns.set(font_scale=2)
```

### References:
* [https://seaborn.pydata.org/tutorial/aesthetics.html](https://seaborn.pydata.org/tutorial/aesthetics.html)
