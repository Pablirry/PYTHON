'''
Return True if the string "cat" and "dog" appear the same number of times in the given string
'''

def cat_dog(str):
    return str.count("cat") == str.count("dog")

print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))