# A few examples how while and for loops work

i = 1
while i <= 50:
    print(i)
    i += 1

for i in range(1, 51):
    print(i)

total = 0
for x in range(1, 31):
    total = total + x
print("Summa: ", total)

for year in range(2005, 2011):
    print(year, end=" ")
