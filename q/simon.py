def solution(A):
    n = len(A)
    
    # Edge cases
    if n < 2:
        return 0
    
    # Calculate sum for each possible tile position (pair of adjacent elements)
    pairs = []
    for i in range(n - 1):
        pairs.append((A[i] + A[i + 1], i))
    
    # If we can only place 1 or 2 tiles
    if n < 4:
        return max(pairs)[0]
    
    # For general case: use DP to find best combination of up to 3 non-overlapping tiles
    # dp[i][k] = maximum sum using at most k tiles from first i pairs
    num_pairs = len(pairs)
    
    # We need at most 3 tiles
    max_tiles = min(3, num_pairs)
    
    # dp[i][k] represents max sum using at most k tiles considering pairs 0..i-1
    dp = [[0] * (max_tiles + 1) for _ in range(num_pairs + 1)]
    
    for i in range(1, num_pairs + 1):
        pair_sum, pair_start = pairs[i - 1]
        
        for k in range(1, max_tiles + 1):
            # Option 1: Don't use this pair
            dp[i][k] = dp[i - 1][k]
            
            # Option 2: Use this pair
            # We need to find the last pair that doesn't overlap with current pair
            # Current pair covers positions [pair_start, pair_start + 1]
            # Previous pair must end before pair_start
            # Previous pair at index j covers positions [j, j+1]
            # So we need j + 1 < pair_start, which means j < pair_start
            # Which means pair index j <= pair_start - 1
            
            if i >= 2 and pair_start >= 1:
                # Can potentially use a previous non-overlapping pair
                dp[i][k] = max(dp[i][k], dp[pair_start][k - 1] + pair_sum)
            elif k == 1:
                # First tile
                dp[i][k] = max(dp[i][k], pair_sum)
    
    return dp[num_pairs][max_tiles]


# Test cases
def test_solution():
    # Test case 1: Example with clear optimal solution
    A1 = [4, 42, 2, 3, 8]
    print(f"Test 1: A = {A1}")
    print(f"Result: {solution(A1)}")
    print(f"Expected: 50 (tiles at [1-2]: 42+2=44, [3-4]: 3+8=11, total=55) or")
    print(f"         54 (tiles at [0-1]: 4+42=46, [3-4]: 3+8=11, total=57) or")
    print(f"         46 (tile at [0-1]: 4+42=46)")
    print()
    
    # Test case 2: Small array
    A2 = [1, 2]
    print(f"Test 2: A = {A2}")
    print(f"Result: {solution(A2)}")
    print(f"Expected: 3 (one tile covering both elements)")
    print()
    
    # Test case 3: All negative numbers
    A3 = [-5, -2, -8, -1]
    print(f"Test 3: A = {A3}")
    print(f"Result: {solution(A3)}")
    print(f"Expected: -3 (tile at [2-3]: -8+(-1)=-9 is worst, [1-2]: -2+(-8)=-10, best is [0-1]: -5+(-2)=-7)")
    print()
    
    # Test case 4: Longer array
    A4 = [5, 3, 2, 9, 1, 7, 6, 4]
    print(f"Test 4: A = {A4}")
    print(f"Result: {solution(A4)}")
    print()
    
    # Test case 5: Only one element
    A5 = [100]
    print(f"Test 5: A = {A5}")
    print(f"Result: {solution(A5)}")
    print(f"Expected: 0 (cannot place any tile)")
    print()
    
    # Test case 6: Three elements
    A6 = [10, 20, 30]
    print(f"Test 6: A = {A6}")
    print(f"Result: {solution(A6)}")
    print(f"Expected: 50 (tile at [1-2]: 20+30=50)")
    print()

if __name__ == "__main__":
    test_solution()