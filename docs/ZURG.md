<a id="zurg"></a>

# zurg

<a id="zurg.one_returns"></a>

#### one\_returns

```python
def one_returns(not_across: List[int], across: List[int], time_spent: int,
                time_limit: int, accumulator: list) -> List[list]
```

Splits the search problem by every toy that could return across the bridge with the flashlight. Terminates early if the time limit for getting all the toys across the bridge is exceeded. Also terminates if all the toys are across the bridge.

**Arguments**:

- `not_across` (`List[int]`): Toys not yet across the bridge
- `across` (`List[int]`): Toys across the bridge
- `time_spent` (`int`): Time spent so far crossing the bridge
- `time_limit` (`int`): Time toys must all be across the bridge by
- `accumulator` (`list`): Partial solution being explored

**Returns**:

`List[list]`: A list of solutions

<a id="zurg.two_cross"></a>

#### two\_cross

```python
def two_cross(not_across: List[int], across: List[int], time_spent: int,
              time_limit: int, accumulator: list) -> List[list]
```

Splits the search problem by every pair of toys that could cross the bridge. Terminates early if the time limit for getting all the toys across the bridge is exceeded.

**Arguments**:

- `not_across` (`List[int]`): Toys not yet across the bridge
- `across` (`List[int]`): Toys across the bridge
- `time_spent` (`int`): Time spent so far crossing the bridge
- `time_limit` (`int`): Time toys must all be across the bridge by
- `accumulator` (`list`): Partial solution being explored

**Returns**:

`List[list]`: A list of solutions

<a id="zurg.zurg"></a>

#### zurg

```python
def zurg() -> List[list]
```

Solves the "Escape from Zurg" puzzle.

**Returns**:

`List[list]`: A list of solutions

