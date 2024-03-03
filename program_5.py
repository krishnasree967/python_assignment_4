# Create a recursive function
# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
# A recursive function is a function that calls itself again and again.

def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)

result = recursive_sum(10)
print("Sum of numbers from 0 to 10 is:", result)