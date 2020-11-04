# Statement

Implement a decorator which will be used on any function taking one int as
a parameter.
The decorator performs a filter on the decorated function:
If the parameter is even, the decorated function is executed and its result
returned.
If the param is odd, the decorated function should not be executed and a
`ValueError` should be raised.
