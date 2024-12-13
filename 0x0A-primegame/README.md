# Prime Game

## Overview

**Prime Game** is a Python-based game that revolves around the strategic removal of prime numbers. The game involves two players, Ben and Maria, competing over a series of rounds to determine the winner.

## How It Works

The game is played as follows:
1. There are multiple rounds, each associated with a number `n`.
2. For each round, the players are given a set of consecutive integers from `1` to `n`.
3. Players take turns removing prime numbers from the set. After removing a prime number, all its multiples are also removed.
4. The player unable to make a move loses the round.

At the end of all rounds, the player who has won the most rounds is declared the overall winner.

## Implementation

This game is implemented in Python using the following key functions:

- **`isWinner(x, nums)`**:
  - Determines the winner of the game after `x` rounds.
  - Accepts two arguments:
    - `x`: The number of rounds.
    - `nums`: A list of integers, where each integer `n` represents the size of the set for the corresponding round.
  - Returns:
    - The name of the player who won the most rounds ("Ben" or "Maria"), or `None` if there is no winner.

- **`rm_multiples(ls, x)`**:
  - Removes multiples of a given prime number from a list of potential prime numbers.

The implementation uses the Sieve of Eratosthenes algorithm to efficiently identify prime numbers.

## Usage

### Prerequisites

- Python 3.7+

### Running the Code

1. Save the game code in a file named `prime_game.py`.
2. Import the `isWinner` function into your script or interactive session:

   ```python
   from prime_game import isWinner
   ```

3. Call the function with the desired number of rounds and set sizes. For example:

   ```python
   x = 3
   nums = [4, 5, 6]
   winner = isWinner(x, nums)
   print(f"The winner is: {winner}")
   ```

### Example

Input:
```python
x = 3
nums = [4, 5, 6]
```

Output:
```
The winner is: Maria
```

## Code Explanation

### Sieve of Eratosthenes
The code uses the Sieve of Eratosthenes to precompute prime numbers efficiently. A list is initialized with all values set to 1 (indicating potential primes), and non-prime indices are set to 0 as their multiples are removed.

### Game Logic
The `isWinner` function:
1. Validates inputs to ensure correct parameters.
2. Uses the precomputed prime numbers to determine the winner of each round based on the count of prime numbers.
3. Tracks and compares the total wins of both players to declare the final winner.

## Notes

- Ensure that the input list `nums` has a length equal to the number of rounds `x`.
- If the game cannot determine a winner (e.g., tied rounds), the function will return `None`.

## License

This project is open-source and available under the MIT License.
