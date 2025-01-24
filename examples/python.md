# Basics to get started with Python
<p>
Python was the first language I programmed with back in the university. I was 
studying English as my major and decided to take a beginner programming course
just for fun. During that course I learned to code very simple code with 
Python and really enjoyed the course. A few years later I am studying 
ICT Engineering and constatly learning more about programming!

Here you can find simple examples of how to code with Python, these examples
are my own code that I have learned dusring my studies.
</p>

## TSTI


> def alvinhinta(summa):
>   hinta = summa * 1.24
>   return round(hinta, 2)

```python
def alvinhinta(summa):
    hinta = summa * 1.24
    return round(hinta, 2)


summa1 = float(input("Anna hinta ilman alv: "))
alvsumma = alvinhinta(summa1)
print(f"Hinta alvin kanssa: {alvsumma} €")
```
