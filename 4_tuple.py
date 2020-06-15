"""
Python Tuples

A tuple is another sequence data type that is similar to the list. 
A tuple consists of a number of values separated by commas. 
Unlike lists, however, tuples are enclosed within parenthesis.

The main difference between lists and tuples are − 
Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, 
while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. 
Tuples can be thought of as read-only lists. 
For example −
"""

tuple = ('abcd', 786, 2.23 , 'john', 70.2)
tinytuple = (123, 'john')

print(tuple) # mencetak semua isi tupel
print(tuple[0]) #mencetak elemen pertama dari tupel
print(tuple[1:3]) #mencetak element dimulai dari index ke 2 sampai index ke 3
print(tuple[2:]) #mencetak elemen dimulai dari index ke3
print(tinytuple * 2) # mencetak 2x isi variabel tinytuple
print (tuple + tinytuple) # menggabungkan semua tuple