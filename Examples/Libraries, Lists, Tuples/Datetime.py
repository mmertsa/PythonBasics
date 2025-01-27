# Simple example how to use datetime module
from datetime import date
today = date.today()
name = "Matti Meikäläinen"
birthyear = 1995
saldo = 8000

print(name, "(", str(birthyear), "),", "saldo: ", str(saldo), "€,", "päivitetty: ", today)
