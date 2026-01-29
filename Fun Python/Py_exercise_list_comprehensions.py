# QUESTION: Write a single-line list comprehension that takes a list of strings, filters out strings shorter than 4 characters, and converts the remaining strings to uppercase.
# Exercise Purpose: List comprehensions are a hallmark of Pythonic code. They allow you to replace verbose for loops and .append() calls with a readable, optimized single line. This exercise teaches you how to combine transformation (uppercase) and filtering (length check) in one expression.
# INPUT: ["apple", "bat", "cherry", "dog", "elderberry"]
# OUTPUT: ['APPLE', 'CHERRY', 'ELDERBERRY']

# MY ANALYSIS
# Deliverable: String list comprehension
# Accepts a string list
# Filters out strings with length less than 4
# Converts the filtered values to uppercase

def transform_strings(x):
  result = [a.upper() for a in x if len(a) >= 4]
  
  return result
  
output = transform_strings(["apple", "bat", "cherry", "dog", "elderberry"])
print(output)
