"""
Python Dictionary

Python's dictionaries are kind of hash-table type. 
They work like associative arrays or hashes found in 
Perl and consist of key-value pairs. A dictionary key 
can be almost any Python type, but are usually numbers 
or strings. Values, on the other hand, can be any arbitrary 
Python object.

Dictionaries are enclosed by curly braces ({ }) and values 
can be assigned and accessed using square braces ([]). 
For example −
"""

dict = {}
dict['one'] = 'This is one'
dict[2] = 'This is two'

tinydict = {'name': 'john', 'code' : 6734, 'dept': 'sales'}

print (dict['one']) #mencetak nilai untuk 1 kunci
print (dict[2]) # mencetak nilai untuk 2 kunci
print (tinydict) #mencetak kamus komplit
print (tinydict.keys()) # mencetak semua kunci
print (tinydict.values()) #mencetak se,mua nilai