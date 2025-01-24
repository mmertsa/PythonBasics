# Basics to get started with Python

Here you can find very basic examples programmed with python.
These examples are done by me and I wanted to share them here to see my own 
progress as I progress with my programming skills. Maybe they can help
you too if you are a beginner with Python!

## Printing and using variables

With Python you can print text simply using print command and writing
the text you want to print as output inside brackets. 

Additionally, you can save 

Identitation is extremely important with Python as Python uses identitation
as a guide to execute code. With identitation you indicate where a new block
of code starts.

```python
nimi = ""
vuosi = 1995
osoite = "Kotikatu 123"

print(f"Hello World!\n{nimi}\n{vuosi}\n{osoite}")
```

```python
def alvinhinta(summa):
    hinta = summa * 1.24
    return round(hinta, 2)


summa1 = float(input("Anna hinta ilman alv: "))
alvsumma = alvinhinta(summa1)
print(f"Hinta alvin kanssa: {alvsumma} €")
```
