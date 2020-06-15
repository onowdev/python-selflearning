"""
Python Lists

Lists are the most versatile of Python's 
compound data types. A list contains items 
separated by commas and enclosed within square 
brackets ([]). To some extent, lists are similar 
to arrays in C. One of the differences between 
them is that all the items belonging to a list 
can be of different data type.

The values stored in a list can be accessed using 
the slice operator ([ ] and [:]) with indexes starting 
at 0 in the beginning of the list and working their way 
to end -1. The plus (+) sign is the list concatenation 
operator, and the asterisk (*) is the repetition operator. 
For example −

"""


list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print (list) #mencetak list semua yg di dalam variabel list
print (list[0]) #mencetak elemen pertama dari list
print (list[1:3]) #mencetak elemen dimulai dari index ke 2 samapi 3
print (list[2:]) #print element dimulai dari index ke 3
print (tinylist *2) # mencetak variabel yang ada di tinylist
print (list + tinylist) # menggabungkan ke 2 list tersebut 