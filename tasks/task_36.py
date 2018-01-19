def function(one, two, three):
    print 'Function called with:', one, two, three
    
# This will work just fine
args = [1, 2, 3]
function(*args)

# This will work just fine, as well
args = '456'
function(*args)

# Call a function with any number of arguments given
def call(f, args):
    # Unpack the list of args and give to the function
    # The cool thing is that we don't have to know how many arguments
    # the function takes, we just use the * operator and it unpacks them for us.
    f(*args)
    

# Pass in our function and arguments
args = [7, 8, 9]
call(function, args)