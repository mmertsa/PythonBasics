def taxprice(total):
    price = total * 1.24
    return round(price, 2)

pricelinput = float(input("Enter price without tax: "))
taxtotal = taxprice(pricelinput)
print(f"The price with tax is: {taxtotal} €")
