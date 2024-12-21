
def recursive_sum(*nums):
    if not nums:
        return 0
    return recursive_sum(*nums[1:]) + nums[0]
print(recursive_sum(1,2,3))