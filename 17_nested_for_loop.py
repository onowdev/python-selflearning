i = 2
while (i<25):
    j=2
    while(j<=(i/j)):
        if not (i%j): break
        j = j + 1
    if (j > i/j): print(i, "is Prime")
    i = i + 1

print("Good Job")