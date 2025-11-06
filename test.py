def is_palindrome(number):
    """
    Checks if a number is a palindrome.
    A palindrome number reads the same forwards and backwards.
    """
    # Convert the number to a string to easily reverse it
    num_str = str(number)
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

def is_prime(number):
    """
    Checks if a number is a prime number.
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    # Check if divisible by 2 or 3
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    # Optimization: check divisors in a specific range (6k +/- 1)
    # We only need to check up to the square root of the number
    # i = 5
    # while i * i <= number:
    #     if number % i == 0 or number % (i + 2) == 0:
    #         return False
    #     i += 6
        
    return True

# --- Example Usage ---
num1 = 121
num2 = 13
num3 = 17

print(f"Number: {num1}")
print(f"Is Palindrome? {is_palindrome(num1)}")
print(f"Is Prime? {is_prime(num1)}")

print("-" * 20)

print(f"Number: {num2}")
print(f"Is Palindrome? {is_palindrome(num2)}")
print(f"Is Prime? {is_prime(num2)}")

print("-" * 20)

print(f"Number: {num3}")
print(f"Is Palindrome? {is_palindrome(num3)}")
print(f"Is Prime? {is_prime(num3)}")


def flatten_recursive(nested_list):
    """
    Flattens a nested list recursively.
    """
    flattened_list = []
    for element in nested_list:
        if isinstance(element, list):
            # If the element is a list, extend the result with the flattened version of that sublist
            flattened_list.extend(flatten_recursive(element))
        else:
            # If it's a single item, append it directly
            flattened_list.append(element)
    return flattened_list

def flatten_list(nested_list):
    for element in nested_list:
        if isinstance(element, list):
            yield from flatten_list(element)
        else:
            yield element

# Example Usage:
nested = [1, [2, 3], [4, [5, 6, [7, 8]]], 9]
print(f"Original: {nested}")
print(f"Flattened: {flatten_recursive(nested)}")
print(f"Flattened: {list(flatten_list(nested))}")
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_nested= [
    [1,2,3,4,5],
    [34,454,5645,2,1,4,6],
    [23,34,56,90,100],
    [1,2,65,90,100]
]

merge_list = [item for sub_list in list_nested for item in sub_list]
print(f"Merged List: {merge_list}")
remove_duplicates = list(set(merge_list))
print(f"Removed Duplicates: {remove_duplicates}")
sorted_list = sorted(remove_duplicates, reverse=True)
print(f"Sorted List: {sorted_list}")


import pandas as pd
import numpy as np

def find_nth_highest_salary(df, n):
    """
    Finds the Nth highest salary in a Pandas DataFrame.
    """
    # 1. Get unique salaries and sort them in descending order
    unique_salaries = df['Salary'].unique()
    
    # Check if there are enough unique salaries for the requested N
    if len(unique_salaries) < n:
        print(f"Error: Not enough unique salaries to find the {n}th highest.")
        return None
    
    # 2. Sort the unique salaries descending
    sorted_salaries = np.sort(unique_salaries)[::-1]
    
    # 3. Return the Nth element (index N-1)
    return sorted_salaries[n - 1]

# --- Example Usage ---
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Salary': [50000, 60000, 75000, 60000, 80000]
}
employees_df = pd.DataFrame(data)

# Find the 3rd highest salary (should be 60000)
N = 3
third_highest = find_nth_highest_salary(employees_df, N)

print(f"DataFrame:\n{employees_df}")
print(f"\nThe {N}th highest salary is: {third_highest}")

salary_list = data['Salary']
unique_salaries = list(set(salary_list))
nth_salary = sorted(unique_salaries, reverse=True)[N-1]
print(f"The {N}th highest salary from list is: {nth_salary}")
