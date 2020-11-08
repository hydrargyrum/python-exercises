# Statement
Implement a class which is a dict but which stores only weak references to
its values.
If only the dict points to one of the values, the class should raise a
`KeyError` as if was not present in the dict. Also, the dict should not hold
references to values objects.
Do not use `weakref.WeakValueDictionary`.

## Hint

- Subclass `dict`
- Implement `__setitem__`
- Implement `__getitem__`
- Delete a key when the object is no longer referenced (may be lazy)
