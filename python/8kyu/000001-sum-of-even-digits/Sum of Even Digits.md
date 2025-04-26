# 8kyu Kata — Sum of Even Digits

**Tags:**  
#numbers #iteration #math #8kyu 

---

## Prompt

Given a non-negative integer `n`, return the sum of all even digits in the number. If there are no even digits, return 0.

#### Real world application
This kata helps in understanding digit manipulation, which is useful in data validation, checksum calculations, and number processing tasks.

---

## Input

- `n`: non-negative integer (0 ≤ n ≤ 10^9)

---

## Output

- Integer representing the sum of all even digits in `n`
- Return 0 if there are no even digits

---

## Examples

```python
sum_even_digits(1234) ➞ 6    # 2 + 4 = 6
sum_even_digits(13579) ➞ 0   # No even digits
sum_even_digits(2468) ➞ 20   # 2 + 4 + 6 + 8 = 20
sum_even_digits(0) ➞ 0       # Single digit 0
```

---

## Notes

- Consider 0 as an even digit
- The input number can be 0
- The solution should work with numbers up to 10^9 