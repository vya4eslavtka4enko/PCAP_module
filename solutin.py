Sample solution: Creating own modules
string_utils.py

import math
 
def halve_string(input_string):
    middle = math.ceil(len(input_string)/2)
    return (input_string[:middle], input_string[middle:])


strings_utils.py

import string_utils
 
def halve_strings(string_list):
    to_return = []
    for string in string_list:
        to_return.append(string_utils.halve_string(string))
    return to_return


main_program.py

import strings_utils
 
quotes = ['Being happy never goes out of style.',
'Life is either a great adventure or nothing.',
'All you need in this life is ignorance and confidence; then success is sure.',
'All your life, you will be faced with a choice. You can choose love or hate... I choose love.',
'The time is always right to do what is right.']
 
print(strings_utils.halve_strings(quotes))