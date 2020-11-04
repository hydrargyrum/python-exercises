# Statement
Implement a class which is a list that is always sorted.
It should support `len()`, access with `[n]`, test with `in` operator and
iteration.
Adding an item with `add` method should insert it in the right position so the
list stays sorted.
Use the `bisect` module as help.
Methods like `index`, `remove` should be implemented too.


# Hint

- Subclassing `list` is possible but discouraged because it would still expose
  the `append` and `insert` methods, which can make the list unsorted.
  Rather use a `data` attribute which is the `list`.
- Implement `__len__`, `__iter__` and `__getitem__` as simple wrappers to
  `data` attribute.
- Implement `index` (like `list.index` method) using `bisect.bisect_left`
- Implement `add` usinb `bisect.insort_left`
- Subclass `collections.abc.Sequence` for avoiding implementing
