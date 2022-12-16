# Things I learned

- Python's `isinstance()` function can be used to check the type of an object.
  - It was useful for turning ints into lists for comparisons
- Python's `sorted()` function can sort using a custom comparison function.
  - It was useful for reusing the already made, custom `compare()` function from
    part 1 to sort all the packets for part 2.
  - Allowed me to remove the quicksort implementation I had originally.
- You can use `cmp_to_key()` from the `functools` library to use your custom
  comparison function to generate keys for the `sorted()` function above.
- It's often useful for a comparison function to return one of three values
  (positive, 0 ,negative) instead of just true or false.
  - This was useful when the compared items inside of a recursion were equal to
    each other and I wanted to continue iterating out of the recursion and not
    just bubble up `true` or `false`.
  - Relating to the above, originally I tried returning `true` when
    `left <= right`, but then when I bubbled out of the recursion, it was
    ambiguous whether the returned true was because `left < right` or
    `left == right`. The distinction was important for logic flow afterwards.
