
def make_equation(*nums):
    if len(nums) == 1:
        return f'{nums[0]}'
    if len(nums) > 1:
        return f'({make_equation(*nums[:-1])}) * x + {nums[-1]}'


print(make_equation(3, 1, 5, 3))
