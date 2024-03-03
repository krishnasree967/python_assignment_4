# Create an inner function to calculate the addition in the following way.

def outer_fun(a, b):
    def inner_fun():
        return a + b
    add = inner_fun() + 5
    return add
result = outer_fun(5, 8)
print(f"Result: {result}")