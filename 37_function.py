# A function is a block of organized, reusable code that is used to perform a single, related action. 
# Functions provide better modularity for your application and a high degree of code reusing.
# As you already know, Python gives you many built-in functions like print(), 
# etc. but you can also create your own functions. These functions are called 
# user-defined functions.


def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

# Now you can call printme function
printme("This is first call to the user defined function!")
printme("Again second call to the same function")