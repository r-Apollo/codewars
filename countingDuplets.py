"""
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once 
in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
"""

def duplicate_count(text):
    return len({e for i, e in enumerate(text.lower()) if (e in "".join(text.lower()[i+1:]))})


print(duplicate_count("aAbbbbb"))
