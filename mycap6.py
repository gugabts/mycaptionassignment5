def print_positive_numbers(nums):
    positive_nums = [num for num in nums if num > 0]  # Use list comprehension to filter positive numbers
    print(positive_nums)

# Test cases
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

# Print positive numbers in list1
print("Input:", list1)
print("Output:", end=" ")
print_positive_numbers(list1)

# Print positive numbers in list2
print("Input:", list2)
print("Output:", end=" ")
print_positive_numbers(list2)
