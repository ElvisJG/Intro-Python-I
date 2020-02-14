# Return the "centered" average of an array of ints, which we'll say is the mean average
# of the values, except ignoring the largest and smallest values in the array. If there are
# multiple copies of the smallest value, ignore just one copy, and likewise for the largest value.
# Use int division to produce the final average. You may assume that the array is length 3 or more.
#
# centered_average([1,2,3,4,100]) => 3
# centered_average([1,1,5,5,10,8,7]) => 5
# centered_average([-10,-4,-2,-4,-2,0]) => -3

# Understand
# inputs-outputs
# array length 3 or more numbers
# can have duplicates
# positive or negative numbers
# average = all numbers / len
# array is not sorted

# Plan
# find min/max
# sort array
# search through
# remove numbers
# average
# sum all remaining values
# find length of array
# return sum/length
# import a library

# --Pseudocode
# min = min(list)
# max = max(list)
# sum = sum(list)
# for each in list: add element to total sum
# length = len(list)
# return sum - min - max / length - 2

def centered_average(nums):
    # min_num = min(nums)
    # max_num = max(nums)
    # total_sum = sum(nums)
    # length = len(nums)
    #
    # return int((total_sum - min_num - max_num) / (length - 2))
    return int((sum(nums) - min(nums) - max(nums)) / (len(nums) - 2))


print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))
print(centered_average([-20, -25, 5, 18, 22, 21.2]))
