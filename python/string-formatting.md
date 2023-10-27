# String formatting in Python

## F-strings (Python >=3.6)

F-strings are faster than the other string formatting methods and are easier to read and use. Here are some tricks you may not have known.

```python
name = "Test"
f'My app name is {name}.'  # 'My app name is Test.
```

### 1. Number formatting:

You can do various formatting with numbers.

```python
number = 150

# decimal places to n -> .nf
print(f"number: {number:.2f}")
# number: 150.00

# hex conversion
print(f"hex: {number:#0x}")
# hex: 0x96

# binary conversion
print(f"binary: {number:b}")
# binary: 10010110

# octal conversion
print(f"octal: {number:o}")
# octal: 226

# scientific notation
print(f"scientific: {number:e}")
# scientific: 1.500000e+02

# total number of characters
print(f"Number: {number:09}")
# Number: 000000150

ratio = 1 / 2
# percentage with 2 decimal places
print(f"percentage = {ratio:.2%}")
# percentage = 50.00%
```

### 2. Stop writing print(f”var = {var}”)

This is the debug feature with f-strings.

```python
a, b = 5, 15
print(f"a = {a}") # Doing this ?
# a = 5

# Do this instead.
print(f"{a = }")
# a = 5

# Arithmatic operations
print(f"{a + b = }")
# a + b = 20

# with formatting
print(f"{a + b = :.2f}")
# a + b = 20.00
```

### 3. Date formatting

You can do `strftime()` formattings from f-string.

```python
import datetime

today = datetime.datetime.now()
print(f"datetime : {today}")
# datetime : 2023-10-27 11:05:40.282314

print(f"date time: {today:%m/%d/%Y %H:%M:%S}")
# date time: 10/27/2023 11:05:40

print(f"date: {today:%m/%d/%Y}")
# date: 10/27/2023

print(f"time: {today:%H:%M:%S %p}")
# time: 11:05:40 AM
```

## Old method (Python >=2.6)
```python
'{} {}'.format('one', 'two')  # Output: 'one two'
'{} {}'.format(1, 2)  # Output: '1 2'
```

## Very old method
```python
'%s %s' % ('one', 'two')  # Output: 'one two'
'%d %d' % (1, 2)  # Output: '1 2'
```

## Number formatting

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
