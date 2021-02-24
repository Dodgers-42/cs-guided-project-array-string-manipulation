# in plcae will modify the array thats passed in to the function
def double_nums_in_place(int_list):
    for idx, item in enumerate(int_list):
        int_list[idx] = item * 2


some_array = [3, 7, 2, 10, 12]
print(some_array)

def double_nums_in_place(int_list):
    # Create a new array, and modify it, then we must return it!
    double_array = [None] * len(int_list)
    for idx in range (len(doubleed_array)):
        item = int_list[idx]
        double_array[idx] = item * 2

    return double_array

some_array = [3, 7, 2, 10, 12]
# double_nums_in_place(some_array)
print(some_array)
doubled_array = double_nums_in_place(some_array)
print(some_array)
print(doubled_array)
