weight = input("weight: ")
choice = input("lb or kg: ")

if choice == 'kg':
    kilo = int(weight) * 0.4536
    print(f'you are {kilo} kg')
elif choice == 'lb':
    pounds = int(weight)/0.45
    print(f'you are {pounds} lbs')
else:
    print(f'you entered wrong choice. choose lb or kg')
