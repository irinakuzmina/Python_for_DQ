# Task 1. Create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter, dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

import random  # to import random module which is used to generate random numbers
import string  # to import string module which to use string.ascii_lowercase constants to return lowercase letters
rand_list = []
for i in range(random.randint(2, 10)):  # loop to add dictionaries to the list with append() method
    rand_dict = {}
    for j in range(0, 3):  # loop to add pairs key-value to each dictionary
        rand_dict.update({random.choice(string.ascii_lowercase): random.randint(0, 100)})  # to add pairs key-value
    rand_list.append(rand_dict)  # to add dictionaries to the list with append() method
print(rand_list)  # to print to console created list of dictionaries

# Task 2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is, example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

common_dict = {}  # to create empty dictionary

h_list = rand_list

for i in rand_list:  # loop to check each dictionary from rand_list
    h_list = [
        item for item in h_list if item != i
    ]  # list comprehension iteratively removing items from h_list
    print(h_list)  # to check h_list in console
    if len(h_list) != 0:  # statement to check if h_list is not empty
        for k in h_list:  # loop to check each dictionary in h_list
            for key, value in i.items():  # to compare keys from current dictionary with others
                for key1, value1 in k.items():
                    if key == key1:  # if statement
                        if value >= value1:
                            # k.pop(key1)
                            key = key+'_'+str(rand_list.index(i)+1)  # to rename key if 1st value is bigger
                            common_dict.update({key: value})  # to update common_dict with key+value pair
                        else:
                            # i.pop(key)
                            key1 = key1+'_'+str(rand_list.index(k)+1) # to rename key if 2nd value is bigger
                            common_dict.update({key1: value1})
                    else:
                        common_dict.update({key: value})  # to update common_dict with key+value pair if key is unique
    else:
        for key, value in i.items():
            common_dict.update({key: value})  # to add left after comparison pairs to common_dict

print(common_dict)


