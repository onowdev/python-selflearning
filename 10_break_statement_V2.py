no = int(input('Masukan No nya: ....'))
numbers = [11,33,55,39,45,35,75,85,65,77,49,69]

for num in numbers:
    if num == no:
        print('number found in list')
        break
else:
    print('Number not Found in List')