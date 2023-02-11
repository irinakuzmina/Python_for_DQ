
# 1.Create list of 100 random numbers from 0 to 1000
import random  # to import random module which is used to generate random numbers

rand_list = []
n = 100
for i in range(n):  # loop to add items to the end of a given list with append() method
    rand_list.append(random.randint(0, 1000))  # randint() method returns an integer number from the specified range

# to check created list and its length - uncomment 2 lines below
# print(rand_list)
# print(len(rand_list))

# 2.Sort list from min to max (without using sort())
for i in range(len(rand_list)):  # for-loops to compare each list element with others
    for j in range(i + 1, len(rand_list)):

        if rand_list[i] > rand_list[j]:  # if statement to compare elements
            rand_list[i], rand_list[j] = rand_list[j], rand_list[i]  # replace elements to have order from min to max

# to check sorted list and compare it with sort() function use - uncomment 3 lines below
# print(rand_list)
# rand_list.sort()
# print(rand_list)


# 3.Calculate average for even and odd numbers

even_list = []
odd_list = []
for i in range(0, len(rand_list)):  # for-loop to check all list element
    if rand_list[i] % 2 == 0:  # if statement to check whether the element is even or odd using % modulus operator
        even_list.append(rand_list[i])  # to add even items to the end of a even_list with append() method
    else:
        odd_list.append(rand_list[i])   # else add odd items to the end of a odd_list with append() method

# to check created lists - uncomment 2 lines below
# print(even_list)
# print(odd_list)

ave_even = sum(even_list) / len(even_list)  # calculate average of even_list
ave_odd = sum(odd_list) / len(odd_list)  # calculate average of odd_list

# 4.Print both average result in console

print("Average of even numbers of list is", ave_even)  # print average of even numbers to console
print("Average of odd numbers of list is", ave_odd)  # print average of odd numbers to console
