"""
Given N arrays,
the task is to print all the elements which are present in at least M arrays
"""
common_elements_dict = dict()


def add_in_dict(arr, arr_num):
    for i in arr:
        if i in common_elements_dict:
            common_elements_dict[i].add(arr_num)
        else:
            common_elements_dict[i] = {arr_num}


def get_common_elements_list(common_elements_factor):
    ret_arr = list()
    for x, y in common_elements_dict.items():
        if len(y) >= common_elements_factor:
            ret_arr.append(x)
    return ret_arr


def main():
    num_of_lists = int(input("Enter number of lists: "))
    common_elements_factor = int(input("From how many lists the elements should be common: "))
    input_list = list()

    for i in range(num_of_lists):
        list_size = int(input("Enter size of " + str(i+1) + "th list: "))
        print("Enter each values on new line for list" + str(i+1) + ": ")
        for j in range(list_size):
            input_list.append(int(input()))
        add_in_dict(input_list, i)
        input_list.clear()

    print("Common elements present in at least " + str(common_elements_factor) + "lists are: \n" +
          str(get_common_elements_list(common_elements_factor)))


main()
