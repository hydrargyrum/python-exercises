# Statement
Implement a class whose constructor takes start and stop like `range`.
It should be iterable to return numbers like `range`.
It sĥould support accessing random elements with `[n]`.
It should support checking length with `len()`.
It should support the `in` operator.
Warning: very big numbers can be passed to constructor, it should not build a list.


# Hint
- Implement `__len__`
- Implement `__iter__`
- Implement `__contains__`
- Implement `__getitem__`
