foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo) 

# prints bar because that is the global variable. 'qux' only exists in the function as a local variable 