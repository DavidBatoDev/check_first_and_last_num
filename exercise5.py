numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

# define a function
def check_first_and_last_item(lst):
    print(f"Given List: {lst}")
    # create 2 variables one for the first item, second is the last item
    first_item = lst[0]
    last_item = lst[-1]
# if first item and second item is same, funtion returns true
    if first_item == last_item:
        return True
# otherwise, function returns false
    else:
        return False
    

# Test:
test1 = check_first_and_last_item(numbers_x)
print(f'The result is {test1}')
test2 = check_first_and_last_item(numbers_y)
print(f'The result is {test2}')

# Output:
# Given List: [10, 20, 30, 40, 10]
# The result is True
# Given List: [75, 65, 35, 75, 30]
# The result is False