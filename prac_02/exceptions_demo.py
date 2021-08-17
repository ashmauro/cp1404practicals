# CP1404/CP5632 - Practical
# Answer the following questions:

# 1. When will a ValueError occur?
# The ValueError will occur when the numerator or denominator are not whole integers.

# 2. When will a ZeroDivisionError occur?
# The ZeroDivisionError will occur when the denominator input is zero.

# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# You could do an if statement to validate the number in the denominator


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
        fraction = numerator / denominator
        print(fraction)
    else:
        print("Cannot divide by zero!")

except ValueError:
    print("Numerator and denominator must be valid numbers!")
#except ZeroDivisionError:
    #print("Cannot divide by zero!")
print("Finished.")
