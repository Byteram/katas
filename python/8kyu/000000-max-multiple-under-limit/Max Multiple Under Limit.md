# 8kyu Kata — Max Multiple Under Limit

**Tags:**  
#logic #math #algorithm #8kyu 

---

## Prompt

Given two positive integers `divisor` and `limit`, return the **largest number less than or equal to `limit`** that is divisible by `divisor`.

#### Real world application
This kata is useful in real-world scenarios like calculating the biggest packet size, batch size, or file chunk that fits under a system constraint.

---

## Input

- `divisor`: integer > 0  
- `limit`: integer ≥ 0

---

## Output

- Integer `n` such that:
  - `n % divisor == 0`
  - `n <= limit`
  - If no such number exists, return `0`.

---

## Examples

```python
max_multiple(3, 10) ➞ 9
max_multiple(7, 20) ➞ 14
max_multiple(5, 25) ➞ 25
max_multiple(5, 2) ➞ 0
```
