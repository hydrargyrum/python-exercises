# Statement
Write a context manager that:
- takes a list as parameter
- appends a number in the list when entering the block and pops it at the
  block end
- pops the number even in case of exception within the block
- can be nested
- the number appended should be the length of the list, starting at 0

# Hint
Use finally for popping.
