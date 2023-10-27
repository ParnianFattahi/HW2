import random

while True:
    R=input(' dice or end: ')
    if R=='end':
        break
    if R=='dice':
      d=random.randint(1,6)
    print(d)
    if d==6:
        d=random.randint(1,6)
        print(d)
    break