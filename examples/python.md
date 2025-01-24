# Basics to get started with Python

- Here you can find very basic examples programmed with python.
- These examples are done by me and I wanted to share them here to see my own 
progress as I progress with my programming skills.
- Maybe they can help you too if you are a beginner with Python!

## Printing and using variables

- With Python you can print text simply using print command and writing
the text you want to print as output inside brackets. 

- Additionally, you can save information or values in variables. The name of 
variable is written first and the value is indicated after equal sign.

- Identitation is extremely important with Python as Python uses identitation
as a guide to execute code. With identitation you indicate where a new block
of code starts.

- Below is an example how to assign values to variables and how to print
the each value in their own line to the terminal. 

```python
name = "John"
year = 1995
address = "Home Street 123"

print(f"Hello World!\n{name}\n{year}\n{address}")
```


## Funcions
¨
User input
round method
tää ehkä väärin

```python
def taxprice(total):
    price = total * 1.24
    return round(price, 2)


total1 = float(input("Anna hinta ilman alv: "))
alvtotal = taxprice(total1)
print(f"Hinta alvin kanssa: {alvtotal} €")
```
