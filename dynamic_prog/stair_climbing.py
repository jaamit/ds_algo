# Number of ways to climb stairs 
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Note: Given n will be a positive integer.

# recursive way
def climbStairs_recursive(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    return climbStairs_recursive(n-1) + climbStairs_recursive(n-2)



# dynamic progamming way
num_ways = [1, 1, 2]
def climbStairs_dp(n: int) -> int:
    if len(num_ways) <= n:
        num_ways.insert(n, (climbStairs_dp(n-1) + climbStairs_dp(n-2)))
    else:
        return num_ways[n]

    return num_ways[n]


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("climbStairs_recursive(10)", setup="from __main__ import climbStairs_recursive"))
    print(timeit.timeit("climbStairs_dp(10)", setup="from __main__ import climbStairs_dp"))

    assert climbStairs_recursive(15) == 987
    assert climbStairs_dp(15) == 987
