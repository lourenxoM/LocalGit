# Python3 code to demonstrate working of
# Dictionary Values Mean
# Using loop + len()

<<<<<<< HEAD
# initializing dictionary
test_dict = {"Gfg" : 5, "is" : 7, "Best" : 8, "for" : 6, "Geeks" : 10}
=======
# initializing dictionary.
test_dict = {"Gfg" : 4, "is" : 7, "Best" : 8, "for" : 6, "Geeks" : 10}
>>>>>>> bf632caddb01aa0ee7bfd62ad90e68b0dee0e965

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# loop to sum all values
res = 0
for val in test_dict.values():
        res += val

# using len() to get total keys for mean computation
res = res / len(test_dict)
