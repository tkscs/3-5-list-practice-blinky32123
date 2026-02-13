print("This is Question 4")

# Create a list of n file names with the format "file_0.txt"

def make_a_list_of_files( count ): 
    # Assign this list to the variable my_list. Then print my_list
    my_list = []

    index = 0
    while index < count:
        my_list.append(f"file_{index}.txt" )
        index = index + 1
    
    print(my_list)

# build a list for count 10
make_a_list_of_files(10)

# build a list for count 1
make_a_list_of_files(1)

# build a list for count 5
make_a_list_of_files(5)
