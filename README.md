# Escape from Zurg: An Implementation in Python

## Overview

"Escape from Zurg" is a Toy Story based puzzle. The puzzle is described in [Escape from Zurg: An Exercise in Logic Programming](https://web.engr.oregonstate.edu/~erwig/papers/Zurg_JFP04.pdf) in which the author compares two solutions, one in Prolog and one in Haskell, to see if functional programming languages are effective for search problems.

Python has an interesting mix of imperative, functional, and OOP features. This project compares the author's Haskell solution to my own Python solution in terms of language features, readability, and performance.


## Implementation


## Testing

To run the "Escape from Zurg" solution, call `make run`. To run the full test suite, run `make test`. To run the tests follow by the solution, run `make`.

Dependencies
* `make`
* `python` >= 3.7 (for `pytest`)
* `pytest`

Within `zurg_test.py` there are system, integration, and unit tests. The `TestZurg` class contains system tests that ensure the solution matches the expected output, derived from `zurg.hs`, a copy of [`ZurgDirect.hs`](https://web.engr.oregonstate.edu/~erwig/zurg/). These are black box tests, as they do not require knowledge of the implementation, just knowledge of the output format.

The `TestTwoCross` and `TestOneReturns` classes contain a mixture of integration and unit tests, where integration tests test the interplay between multiple user defined functions (in this case, `two_cross()` and `one_returns()`), and unit tests test a single user defined function in isolation. Due to the indirectly recursive nature of both `two_cross()` and `one_returns()`, both integration and unit tests make one function call. The distinction is in the behavior triggered by the input parameters. All the `recursive_case` tests are integration tests. Most of the `termination_case` tests are unit tests, with the exception of `TestTwoCross::test_termination_case_solution_found`.

The tests in `TestTwoCross` and `TestOneReturns` are gray box tests. They only need knowledge of the output format for the test cases but need implementation knowledge to distinguish between integration and unit tests.

## Listing

