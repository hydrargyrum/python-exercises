# Statement
Implement a class that has a `fields` attribute which contains the names
of the attributes that can be read/written (except special attributes).
If a test tries to create an additional attribute, it should be prevented.
And don't use `__slots__`.


## Hint

Use `__getattr__`, `__setattr__`.
