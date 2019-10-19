Title: Sorting lists
Date: 2017-11-26 15:10
Authors: José Aniceto


`sorted()` returns a **new** sorted list, leaving the original list unaffected. `list.sort()` sorts the list **in-place**, mutating the list indices, and returns None (like all in-place operations).

`sorted()` works on any iterable, not just lists. Strings, tuples, dictionaries (you'll get the keys), generators, etc., returning a list containing all elements, sorted.

* Use `list.sort()` when you want to mutate the list, sorted() when you want a new sorted object back. Use `sorted()` when you want to sort something that is an iterable, not a list yet.
* For lists, `list.sort()` is faster than `sorted()` because it doesn't have to create a copy. For any other iterable, you have no choice.
* No, you cannot retrieve the original positions. Once you called `list.sort()` the original order is gone.

#### Useful links:
https://stackoverflow.com/questions/22442378/what-is-the-difference-between-sortedlist-vs-list-sort-python
https://stackoverflow.com/questions/18761776/sort-list-of-dictionaries-by-multiple-keys-with-different-ordering
https://stackoverflow.com/questions/16082954/python-how-to-sort-a-list-of-dictionaries-by-several-values
