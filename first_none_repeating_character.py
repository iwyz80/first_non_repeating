def first_non_repeating_character(string):
    """A function to print the first none repeating charater in 
    a string"""
    
    #convert string to lowercase
    string2lower = string.lower()
    repeated = [] # Array to hold repeating characters
    #Iterate through the lowercase string and append characters
    #that are not repeated
    for i in string2lower:
        if string2lower.count(i)== 1:
            repeated.append(string2lower.index(i))
    if repeated!=[]:
        return string[repeated[0]]
    else:
        return ''
print (first_non_repeating_character('eeeee'))