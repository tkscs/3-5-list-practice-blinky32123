
print("This is Question 3")

# Create a list with the following 10 numbers:
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# Assign this list to the variable my_list. Then print my_list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)

# Find and print the average

sum = 0
count = 0

for value in my_list:
    sum = sum + value
    count = count + 1

print(sum / count)