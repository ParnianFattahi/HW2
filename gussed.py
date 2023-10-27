import random

pc_number=random.randint(0, 200)
count=0
while True:
    user_number=int(input('enter number:  '))
    count=count+1
    if user_number== pc_number:
        print('ok')
        break 
    if user_number< pc_number:
        print('adad bozorg tari vared kon')

    if user_number> pc_number:
        print('adad koochak tar vared kon')

print(pc_number)
print('the number of gusse=',count)
