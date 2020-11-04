# Statement
Implement a class of string which is insensitive to case when compared
to other strings (even regular strings).
They should support sorting with case insensivity.
They should support being used as a dict key.

When printed though, they should retain their original casing.


## Hint

- Implement `__eq__`, `__ne__`.
- Implement `__hash__` (always do when you implement `__eq__` for a class).
- Implement `__lt__`, `__le__`, `__gt__`, `__ge__`.
