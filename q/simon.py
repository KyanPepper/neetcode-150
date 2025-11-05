

def solution(A):
   
    n = len(A)
    
    # Edge case: need at least 2 elements to place a tile
    if n < 2:
        return 0
    

    pairs = []
    for i in range(n - 1):
        pairs.append(A[i] + A[i + 1])
    
    num_pairs = len(pairs)
    

    if num_pairs == 1:
        return max(0, pairs[0])  # Return 0 if sum is negative
    

    max_tiles = min(3, num_pairs)
    

    NEG_INF = float('-inf')
    dp = [[NEG_INF] * (max_tiles + 1) for _ in range(num_pairs + 1)]
    

    for i in range(num_pairs + 1):
        dp[i][0] = 0
    
    # Fill DP table
    for i in range(1, num_pairs + 1):
        pair_sum = pairs[i - 1]  # Sum of current pair
        
        for k in range(1, max_tiles + 1):
            # Option 1: Don't use this pair (carry forward previous best)
            dp[i][k] = dp[i - 1][k]
            
            # Option 2: Use this pair
            # If we use pair at index i-1, we cannot use pair at index i-2
            # because they would overlap (pair i-2 covers A[i-2] and A[i-1],
            # and pair i-1 covers A[i-1] and A[i])
            # So we look at dp[i-2][k-1] to get the best sum using k-1 tiles
            # before the previous pair
            if i >= 2:
                dp[i][k] = max(dp[i][k], dp[i - 2][k - 1] + pair_sum)
            else:
                # First pair, no overlap concerns
                if k == 1:
                    dp[i][k] = max(dp[i][k], pair_sum)
    
    # Return the maximum sum achievable using at most max_tiles tiles
    # We check all possibilities from 0 to max_tiles to handle negative sums
    result = 0
    for k in range(max_tiles + 1):
        result = max(result, dp[num_pairs][k])
    
    return result


# Test cases
def test_solution():
    """Run comprehensive test cases"""
    
    tests = [
        {
            'input': [4, 42, 2, 3, 8],
            'expected': 57,
            'description': 'Standard case with multiple tiles'
        },
        {
            'input': [1, 2],
            'expected': 3,
            'description': 'Minimum size array'
        },
        {
            'input': [-5, -2, -8, -1],
            'expected': 0,
            'description': 'All negative numbers - use no tiles'
        },
        {
            'input': [5, 3, 2, 9, 1, 7, 6, 4],
            'expected': 32,
            'description': 'Longer array requiring optimal selection'
        },
        {
            'input': [100],
            'expected': 0,
            'description': 'Single element - cannot place tile'
        },
        {
            'input': [10, 20, 30],
            'expected': 50,
            'description': 'Three elements - one tile optimal'
        },
        {
            'input': [5, -3, 10, 2, -1, 8],
            'expected': 21,
            'description': 'Mix of positive and negative'
        },
        {
            'input': [1, 1, 1, 1, 1, 1],
            'expected': 6,
            'description': 'All elements equal - use 3 tiles'
        },
            {'input': [1,5,3,2,6,6,10,4,7,2,1],
             'expected': 35,
             'description': 'All elements equal'
            }
   


    ]
    
    all_passed = True
    for i, test in enumerate(tests, 1):
        result = solution(test['input'])
        passed = result == test['expected']
        all_passed = all_passed and passed
        
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"Test {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print()
    
    if all_passed:
        print("All tests passed! ✓")
    else:
        print("Some tests failed. ✗")
    
    return all_passed

if __name__ == "__main__":
    test_solution()