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

- Python has multiple useful built-in functions that can be utilized 
- You can also create your own functions that can be run when called
- Functions are defined with def and are called by using the name of <br>
function and adding parenthesis afterwards. If there is a parameter(s) <br>
it is added inside the parenthesis.
- Below there is an example of a simple function which calculates <br>
the price of a product after taxes (24%) are added
- The function takes one parameter (total), which is asked from the <br>
user with a built-in input-function
- Another built-in function, round, is used as well
- Round-function rounds the price to two decimals

```python
def taxprice(total):
    price = total * 1.24
    return round(price, 2)


pricelinput = float(input("Enter price without tax: "))
taxtotal = taxprice(pricelinput)
print(f"The price with tax is: {taxtotal} €")
```
