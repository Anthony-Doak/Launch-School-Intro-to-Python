def set_foo():
    foo = 'bar'

set_foo()
print(foo) 

# We get an error because foo is inside a function and is thus only a local variable that the print statement cannot access 