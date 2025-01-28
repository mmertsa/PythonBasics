# Basics to get started with Python

- Here you can find very basic examples programmed with python.
- These examples are done by me and I wanted to share them here to see my own 
progress.
- Maybe they can help you too if you are a beginner with Python!

## Printing and using variables

- With Python you can print text simply using the print-function and writing
the text you want to print inside parenthesis. 
- Additionally, you can save information or values in variables. The name of the
variable is written first and the value is indicated after an equal sign.
- Identitation is extremely important with Python as Python uses identitation
as a guide to execute code. With identitation it is indicated where a new block
of code starts.
- The example below demonstrates how to assign values to variables and how to print
each value to their own line in the terminal. 

```python
name = "John"
year = 1995
address = "Home Street 123"

print(f"Hello World!\n{name}\n{year}\n{address}")
```


## Functions

- Python has multiple useful built-in functions that can be utilized within <br>
your own code 
- You can also create your own functions that can be run when called
- Functions are defined with def and are called by using the name of <br>
the function and adding parenthesis afterwards. If there is a parameter(s) <br>
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

- Here is another example of a simple function that <br>
calculates the amount of fuel consumption based on the distance <br>
entered by user
- In my examples as the function is called, the return value is also <br>
printed. If it is not printed, the code still runs, the value just is not <br>
visible anywhere


```python
def consumption(distance):
    fuel = (6.5 * distance) / 100
    return round(fuel, 1)

distanceinput = int(input("Enter the distance: "))
print(consumption(distanceinput), "l/100km")
```

- You can find more very simple examples from Examples!

## If- sentences
## For-loop

More notes coming..