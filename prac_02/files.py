# """"1. Write code that asks the user for their name, then opens a file
# called "name.txt" and writes that names too it"""""

user_name = input("What is your name? ")
out_file = open("users_name.txt", 'w')
print(user_name, file=out_file)
out_file.close()

# """ 2. Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file). """

in_file = open('users_name.txt', 'r')
users_name = in_file.read()
users_name = users_name.strip()
in_file.close()
print("Your name is", users_name)

# """Create a text file called numbers.txt and save it in your prac_02 directory.
# Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400
# Write code that opens "numbers.txt", reads only the first two numbers and adds
#  them together then prints the result, which should be... 59."""

in_file = open("numbers.txt", 'r')
first_number = int(in_file.readline())
second_number = int(in_file.readline())
print(f"First number is: {first_number}")
print(f"Second number is: {second_number}")
total = first_number + second_number
print(f"Total is: {total}")

# """4. Now write a fourth block of code that prints the total for all lines in numbers.txt
#  or a file with any number of numbers."""

in_file = open("numbers.txt", 'r')
total_sum = 0
for line in in_file:
    new_number = int(line)
    total_sum += new_number
    print(f"The number is: {new_number}")
print(f"The total sum of these numbers is: {total_sum}")
