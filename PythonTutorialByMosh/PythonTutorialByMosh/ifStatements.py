
'''
is_hot = False
is_cold = True

if is_hot:
    print("Its a hot day!")
    print("Drink plenty of water")
elif is_cold:
    print("Its a cold day")
    print("Wear warm clothes")
else:
    print("Its a normal day.")
    print("Cool")
print("Enjoy your day")
'''

house_price = 1000000
buyer_has_good_credit = True

if buyer_has_good_credit:
    # print((10 * house_price) / 100)
    print(f"DownPayment: {0.1 * house_price}")
else:
    # print((20 * house_price) / 100)
    print(0.2 * house_price)