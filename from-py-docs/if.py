x = int(input("Please Enter An integer:"))

if x < 0:
    x = 0
    print('Negative Changed to Zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('single')
else:
    print('More')