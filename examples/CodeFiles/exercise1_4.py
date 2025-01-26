def kellonaika(aika):
    tunnit = aika // 60
    minuutit = aika % 60
    return f"{tunnit}h {minuutit}min"


aika1 = int(input("Anna minuutit kokonaislukuna: "))
print(kellonaika(aika1))
