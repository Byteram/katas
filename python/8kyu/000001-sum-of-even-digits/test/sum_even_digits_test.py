import time
import random
from app.main import sum_even_digits


def performance(func):
    """
    Decorator to measure and verify the performance of a test function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        assert execution_time < 1.0, (
            f"Performance test failed for {func.__name__}. "
            f"Execution time: {execution_time:.4f} seconds "
            f"(max allowed: 1.0 seconds)"
        )
        print(f"Performance test passed for {func.__name__}. "
              f"Execution time: {execution_time:.4f} seconds")
        return result
    return wrapper


# === Fixed Tests ===
@performance
def test_fixed():
    """
    Test basic cases with known inputs and outputs.
    These tests cover common scenarios and some edge cases.
    """
    assert sum_even_digits(1234) == 6
    assert sum_even_digits(13579) == 0
    assert sum_even_digits(2468) == 20
    assert sum_even_digits(0) == 0
    assert sum_even_digits(42) == 6
    assert sum_even_digits(314159265) == 12
    assert sum_even_digits(987654321) == 20
    assert sum_even_digits(101010101) == 0


# === Edge Case Tests ===
@performance
def test_edge_cases():
    """
    Test boundary conditions and special cases.
    These tests ensure the function handles edge cases correctly.
    """
    assert sum_even_digits(0) == 0
    assert sum_even_digits(1) == 0
    assert sum_even_digits(2) == 2
    assert sum_even_digits(8) == 8
    assert sum_even_digits(9) == 0
    assert sum_even_digits(2468) == 20
    assert sum_even_digits(2222222222) == 20
    assert sum_even_digits(13579) == 0
    assert sum_even_digits(1111111111) == 0
    assert sum_even_digits(1020304050) == 6
    assert sum_even_digits(1234567890) == 20


# === Random Tests ===
@performance
def test_random():
    """
    Test with random inputs to ensure robustness.
    These tests verify the function works correctly with various inputs.
    """
    random.seed(42)
    for _ in range(10000):
        n = random.randint(0, 10**9)
        expected = sum(int(d) for d in str(n) if int(d) % 2 == 0)
        result = sum_even_digits(n)
        assert result == expected, (
            f"Failed for n={n}. "
            f"Expected {expected}, got {result}. "
            f"Digits: {[int(d) for d in str(n)]}, "
            f"Even digits: {[int(d) for d in str(n) if int(d) % 2 == 0]}"
        )

# === Run All Tests ===


@performance
def run_all_tests():
    test_fixed()
    test_edge_cases()
    test_random()


# Run tests
if __name__ == "__main__":
    run_all_tests()
