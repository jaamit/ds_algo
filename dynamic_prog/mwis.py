# Maximum Weight Independent Set of a Path Graph
# The input will be a simple array where each array value is the weight of the corresponding vertex. 
# The output should be an array of indices (zero-based, in-order) of the elements that belong to 
# the maximum weight independent set.
# A few examples:
# Input [1,2,4] represents a path graph that has vertices A--B--C with A=1, B=2, and C=4.
# The independent set {A,C} is the maximum with a value of 5. The expected output is [0,2].
# Input [1,2,3,4] represents a path graph that has vertices A--B--C--D with A=1, B=2, C=3, and D=4. 
# The independent set with {B,D} is the maximum with a value of 6. The expected output is [1,3]
# Input [6,1,2,7,3,5] represents a path graph that has vertices A--B--C--D--E--F with 
# A=6, B=1, C=2, D=7, E=3, and F=5. The independent set with {A,D,F} is the maximum with value of 18. The output is [0,3,5].

# recursive way
def mwis_rec(path):
    if len(path) == 0:
        return 0
    elif len(path) == 1:
        return path[0]
    else:
        max_sum = max(mwis_rec(path[:-1]), (mwis_rec(path[:-2]) + path[-1]))
        return max_sum

assert mwis_rec([1,2,4]) == 5
assert mwis_rec([1,2,3, 4]) == 6
assert mwis_rec([6,1,2,7,3,5]) == 18
assert (mwis_rec([1, 4, 5, 4])) == 8


# dp way
def mwis_dp(path):
    path_sum = [0 for i in range(len(path)+1)] # init result array

    # base case
    path_sum[0] = 0
    path_sum[1] = path[0]

    # optimal sub-problems
    for i in range(2, len(path_sum)):
        path_sum[i] = max(path_sum[i-1], (path_sum[i-2] + path[i-1]))
    
    return path_sum[-1]

assert mwis_dp([1,2,4]) == 5
assert mwis_dp([1,2,3, 4]) == 6
assert mwis_dp([6,1,2,7,3,5]) == 18
assert (mwis_dp([1, 4, 5, 4])) == 8

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("mwis_rec([6,1,2,7,3,5])", setup="from __main__ import mwis_rec"))
    print(timeit.timeit("mwis_dp([6,1,2,7,3,5])", setup="from __main__ import mwis_dp"))

    assert mwis_dp([6,1,2,7,3,5]) == 18
    assert mwis_rec([6,1,2,7,3,5]) == 18