import random
import time
import pytest  # Optional: for better test organization

# === Fixed Tests ===
def test_fixed():
    """
    Test basic cases with known inputs and outputs.
    These tests cover common scenarios and some edge cases.
    """
    assert max_multiple(3, 10) == 9
    assert max_multiple(7, 20) == 14
    assert max_multiple(5, 25) == 25
    assert max_multiple(5, 2) == 0
    assert max_multiple(1, 1) == 1
    assert max_multiple(2, 1) == 0
    assert max_multiple(10, 100) == 100
    assert max_multiple(2, 9) == 8
    assert max_multiple(9, 9) == 9
    assert max_multiple(3, 1) == 0
    print("Fixed tests passed")

# === Edge Case Tests ===
def test_edge_cases():
    """
    Test boundary conditions and special cases.
    These tests ensure the function handles edge cases correctly.
    """
    # When limit is 0
    assert max_multiple(1, 0) == 0
    
    # When divisor equals limit
    assert max_multiple(1000000, 1000000) == 1000000
    
    # When divisor is just less than limit
    assert max_multiple(999999, 1000000) == 999999
    
    # When divisor is larger than limit
    assert max_multiple(10**6, 10**6 - 1) == 0
    
    # When divisor is 1 (always returns limit)
    assert max_multiple(1, 42) == 42
    
    # When divisor is larger than limit
    assert max_multiple(5, 3) == 0
    
    print("Edge cases passed")

# === Random Tests ===
def test_random():
    """
    Test with random inputs to ensure robustness.
    These tests verify the function works correctly with various inputs.
    """
    for _ in range(100):
        divisor = random.randint(1, 10000)
        limit = random.randint(0, 100000)
        expected = limit - (limit % divisor) if limit >= divisor else 0
        result = max_multiple(divisor, limit)
        assert result == expected, (
            f"Failed for divisor={divisor}, limit={limit}. "
            f"Expected {expected}, got {result}. "
            f"Calculation: limit - (limit % divisor) = {limit} - ({limit} % {divisor}) = {expected}"
        )
    print("Random tests passed")

# === Performance Tests ===
def test_performance():
    """
    Test performance with large numbers.
    These tests ensure the function performs well with large inputs.
    """
    start_time = time.time()
    
    # Test with large numbers
    for _ in range(10):
        divisor = random.randint(10**5, 10**6)
        limit = random.randint(10**5, 10**6)
        max_multiple(divisor, limit)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Ensure the function completes within a reasonable time (e.g., 1 second)
    assert execution_time < 1.0, f"Performance test failed. Execution time: {execution_time:.4f} seconds"
    print(f"Performance tests passed. Execution time: {execution_time:.4f} seconds")

# === Run All Tests ===
def run_all_tests():
    """
    Run all test functions in sequence.
    """
    test_fixed()
    test_edge_cases()
    test_random()
    test_performance()
    print("All tests passed successfully.")


# Run tests
if __name__ == "__main__":
    run_all_tests()
