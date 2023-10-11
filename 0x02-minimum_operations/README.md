# 0x02. Minimum Operations

**INTRODUCTION**

This project involves a coding problem that challenges us to find the minimum number of copy and paste operations required to produce a given number of characters in a text file.

## Tasks:page_with_curl:

<h3> 0. Minimum Operations </h3>

**Problem**
- In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

- Requirements
  - Prototype: `def minOperations(n)`
  - Returns an integer
  - If `n` is impossible to achieve, return `0`
**Example:**

`n = 9`

`H` => `Copy All` => `Paste` => `HH` => `Paste` =>`HHH` => `Copy All` => `Paste` => `HHHHHH` => `Past` => `HHHHHHHHH`

Number of operations: `6`

**Solution**

- This problem is akin to finding the prime factors of a number, as each `copy` and `paste` operation can be viewed as multiplying the current number of characters by a factor. For example, if we have `3` characters and we `copy` and `paste` them, we  will obtain `6` characters, which is `3` times `2`. If we then perform another `copy` and `paste` operation, we will have `12` characters, which is `3` times `2` times `2` ... and so on.
- [0-minoperations.py](./0-minoperations.py): A Python code that implements this algorithm.
