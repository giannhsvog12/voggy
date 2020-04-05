
print('hello world')
print('Ας δουμε την προπαιδεια΄')
from random import randint
import random
number = input('Θα δουμε την προπαιδεια του ;')
roll = 0
rdlist = []
for n in range(1, 11):
    k = randint(1,20)
    flag = True
    map = 0
    # μας δινει τυχαια τιμη αλλα να μην την εχουμε ηδη μεσα στην λιστα μας.
    while k in rdlist:
        k = randint(1, 20)
    while k not in rdlist:
        rdlist.append(k)
    answer = input(f'{k} x {number} = ')
    if answer == 'q': exit()
    if int(answer) == int(k * int(number)):
            flag = False
            map = 1
            roll += 1 #το ρολλ μας δινει στην ουσια τον βαθμο  που θα εχουμε στο τελος οταν κανουμε την ασκηση


if roll > 0:
    print(str(roll) + ' στα 10')
else:
    print('0' + ' στα 10 ')





