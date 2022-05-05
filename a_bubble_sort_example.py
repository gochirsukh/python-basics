def bubble_sort(my_list):
    # We go through the list as many times as there are elements
    for i in range(len(my_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(my_list) - 1):
            if my_list[j] > my_list[j+1]:
                # Swap
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                print(my_list)

my_list = [9, 8, 7, 4, 3, 6, 5, 1, 2]
bubble_sort(my_list)
