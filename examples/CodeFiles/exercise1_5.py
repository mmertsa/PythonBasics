def kopakot(sentit):
    viiskyt = sentit // 50
    kakskyt = (sentit % 50) // 20
    kympit = ((sentit % 50) % 20) // 10
    vitoset = ((sentit % 50) % 20) % 10 // 5
    kakoset = (((sentit % 50) % 20) % 10) % 5 // 2
    ykoset = ((((sentit % 50) % 20) % 10) % 5) % 2 // 1
    return (f"50 snt kolikoita {viiskyt} kpl\n20 snt kolikoita {kakskyt} kpl\n"
            f"10 snt kolikoita {kympit} kpl\n5 snt kolikoita {vitoset} kpl\n"
            f"2 snt kolikoita {kakoset} kpl\n1 snt kolikoita {ykoset} kpl")


sentit1 = int(input("Anna 1-100 senttiä: \n"))
print(kopakot(sentit1))
