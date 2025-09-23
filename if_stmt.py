is_hot = False
is_cold = True

if is_hot:
    print("it's hot day\ndrink plenty of water")
elif is_cold:
    print('its cold day\nwear warm clothes')
else:
    print('its lovely day')

print('enjoy ur day')


#example:

print('\n')
price = 1000000
good_credit = True

if good_credit:
    down_paymt = price*0.10
else:
    down_paymt = price*0.20

print('down_payment: $ ', down_paymt)


# and: both conditions true
# or: at least one conditions are true
# not: when you want to negate a condition
# comparatible ops: > | >= | <  | <= | == | !=