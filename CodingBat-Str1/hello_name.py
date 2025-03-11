'''
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
'''

def hello_name(name):
    return "Hello" + " " + name + "!"

print(hello_name('Bob'))
print(hello_name('Alice'))
print(hello_name('X'))