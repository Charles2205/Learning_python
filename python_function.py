# built in functions and user-defined functions
# they are reuseable 

# Why?
# To break down your program into components and stop repeat codes

# When?
# when your codes turns to be plenty and unorganized we use function to break it down
# pass is a keyword means nothing 
#  How (Syntax)
# def functionname (Parameters):
''' docstring
'''
# instructions
def sums(x,y=0):
    """
    This function helps user to add two numbers and display the results
    """
    results = x + y
    return results

a=sums(y=1)
print(a)
