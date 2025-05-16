MOD = 10**9 + 7

def getSum(X, Y, Z):
    # We'll use dynamic programming to track:
    # 1. The sum of all numbers formed so far
    # 2. The count of numbers formed so far
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dp(count4, count5, count6):
        total_sum = 0
        total_numbers = 0
        
        # Try adding digit 4 if we haven't used all available
        if count4 < X:
            sum_add_4, numbers_add_4 = dp(count4 + 1, count5, count6)
            total_sum += sum_add_4 * 10 + 4 * (numbers_add_4 + 1)
            total_numbers += numbers_add_4 + 1
        
        # Try adding digit 5 if we haven't used all available
        if count5 < Y:
            sum_add_5, numbers_add_5 = dp(count4, count5 + 1, count6)
            total_sum += sum_add_5 * 10 + 5 * (numbers_add_5 + 1)
            total_numbers += numbers_add_5 + 1
        
        # Try adding digit 6 if we haven't used all available
        if count6 < Z:
            sum_add_6, numbers_add_6 = dp(count4, count5, count6 + 1)
            total_sum += sum_add_6 * 10 + 6 * (numbers_add_6 + 1)
            total_numbers += numbers_add_6 + 1
        
        return total_sum % MOD, total_numbers % MOD
    total_sum, _ = dp(0, 0, 0)
    return total_sum


print(getSum(1,2,1))

