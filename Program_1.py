"""1. Write a program to compute the frequency of the words from the input.
The output should output after sorting the key alphanumerically.
○ Eg - line = “which is better python 2 or python 3”"""

import operator
input_string = "which is better python 2 or python 3"
dict_Freq = {}  # creating a dict variable to store the frequency of words and numbers
for i in input_string.split(' '):
    if i.isalnum():      #Using isalnum method to compare numbers and alphabets
        if i not in dict_Freq:
            dict_Freq[i] = 1
        else:
            dict_Freq[i] = dict_Freq[i] + 1
print(dict_Freq)
sorted_dict_Freq = sorted(dict_Freq.items(), key = operator.itemgetter(0))   # Using Sorting technique in Dictionary
print(sorted_dict_Freq)

