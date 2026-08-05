def sum_n(n):
    print("Calling sum_n(", n, ")", sep="")

    if n == 1:
        print("Base Case: sum_n(1) = 1")
        return 1

    result = n + sum_n(n - 1)
    print("Returning:", n, "+ sum_n(", n-1, ") =", result, sep="")
    return result

# Input
n = int(input("Enter the value of N: "))

# Function Call
result = sum_n(n)

# Output
print("Sum of first", n, "natural numbers is:", result)
