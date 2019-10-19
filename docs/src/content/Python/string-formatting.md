Title: String formatting in Python
Date: 2017-08-10 22:13
Authors: José Aniceto


### F-strings (Python >=3.6)
```python
name = "Test"
f'My app name is {name}.'  # 'My app name is Test.
```

### New method (Python >=2.6)
```python
'{} {}'.format('one', 'two')  # Output: 'one two'
'{} {}'.format(1, 2)  # Output: '1 2'
```

### Old method
```python
'%s %s' % ('one', 'two')  # Output: 'one two'
'%d %d' % (1, 2)  # Output: '1 2'
```

### Number formatting

The following table shows various ways to format numbers using str.format(), including examples for both float formatting and integers.

To run examples use `print("FORMAT".format(NUMBER))`. So to get the output of the first example, you would run: `print("{:.2f}".format(3.1415926))`.

Number |	Format |	Output |	Description
--- | --- | --- | ---
3.1415926 |	{:.2f} |	3.14 |	2 decimal places
3.1415926 |	{:+.2f} |	+3.14 |	2 decimal places with sign
-1 |	{:+.2f} |	-1.00 |	2 decimal places with sign
2.71828 |	{:.0f} |	3 |	No decimal places
5 |	{:0>2d} |	05 |	Pad number with zeros (left padding, width 2)
5 |	{:x<4d} |	5xxx |	Pad number with x’s (right padding, width 4)
10 |	{:x<4d} |	10xx |	Pad number with x’s (right padding, width 4)
1000000 |	{:,} |	1,000,000 |	Number format with comma separator
0.25 |	{:.2%} |	25.00% |	Format percentage
1000000000 |	{:.2e} |	1.00e+09 |	Exponent notation
13 |	{:10d} |	        13 |	Right aligned (default, width 10)
13 |	{:<10d} |	13 |	Left aligned (width 10)
13 |	{:^10d} |	    13 |	Center aligned (width 10)
