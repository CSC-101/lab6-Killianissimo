import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
'''This function inputs a list of Books and returns a list of Books. This function takes the 
inputted list of Books and sorts them alphabetically with the selection sort method. It is feasible
that the function modifies the list and thus doesn't then need to return the list, but it works 
this way too.
'''
def selection_sort_books(values:list[data.Book]) -> list[data.Book]:
    for i in range(len(values) - 1):
        big_index = i
        for j in range(i+1, len(values)):
            if values[j].title < values[big_index].title:
                big_index = j
        if big_index != i:
            temp = values[i]
            values[i] = values[big_index]
            values[big_index] = temp
    return values

# Part 2
'''This function inputs a string and outputs a string. This function takes the input string and,
for each letter in the string, swaps its case (it makes upper case letters lower case and vice 
versa). It leaves all other characters alone. It returns this new string.
'''
def swap_case(input:str) -> str:
    output = ""
    for i in range(len(input)):
        if input[i].islower() == True:
            output += (input[i].upper())
        elif input[i].isupper() == True:
            output +=(input[i].lower())
        else:
            output += (input[i])
    return output

# Part 3
'''This function inputs a 3 strings, one of any length and two of length 1, and outputs one string.
This function takes the string of any length and replaces all instances of the first length 1
string and replaces them with the second length 1 string. It then returns this new string.
'''
def str_translate(input:str, old:str, new:str) -> str:
    output = ""
    for i in range(len(input)):
        if input[i] == old:
            output += new
        else:
            output += input[i]
    return output

# Part 4
'''This function inputs a string and outputs a dictionary. This function takes the inputted string
and removes all spaces before created a dictionary with a key for each letter that appears and a
corresponding integer that indicates how many times each key appears in the given string. The 
function then returns the dictionary. 
'''
def histogram_letters(para):
    letters = {}
    newPara = ""
    betweenSpaces = para.split()
    for i in range(len(betweenSpaces)):
        for j in range(len(betweenSpaces[i])):
            newPara += betweenSpaces[i][j]
    for i in newPara:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters