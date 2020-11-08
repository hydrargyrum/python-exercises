# Statement

Implement a parametrizable decorator which will be used on any function taking
one int as a parameter.
The decorator takes a number which is a factor.
The decorator performs a filter on the decorated function:
If the parameter is a multiple of the factor, the decorated function is
executed and its result returned.
If the param is not a multiple of the factor, the decorated function should
not be executed and a `ValueError` should be raised.

## Hint

Consider that:

    @accept_only_multiples_of(2)
    def decorated(n):
        ...

is equivalent to:

    def decorated(n):
        return n + 1
    decorated = accept_only_multiples_of(2)(decorated)

So `accept_only_multiples_of(2)` is the equivalent of `accept_only_even` and
`accept_only_multiples_of` is one level more abstract than `accept_only_even`.
It is a function returning a function, which will take a function and return
a function as a result.
