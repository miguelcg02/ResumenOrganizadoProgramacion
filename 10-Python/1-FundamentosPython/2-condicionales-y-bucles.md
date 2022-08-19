# Sentencia if - elif - else

```
if (x == y):
    print('Hola Mundo)
-----------------------------
if (x == y):
    print('igual')
else:
    print('diferente')
-----------------------------
if (x < y):
    print('x menor que y')
elif (x > y):
    print('y menor que x')
else:
    print('igual')
-----------------------------
def SwitchExample(argument):
    switcher = {
        0: " This is Case Zero ",
        1: " This is Case One ",
        2: " This is Case Two ",
    }
    return switcher.get(argument, "nothing")

```

# Bucles

1. While

```
while i < len(lenguajes):
    print(lenguajes[i])
    i += 1
```

2. for (itera sobre la lista)

```
lenguajes = ["Python", "C", "C++", "Java"]

for l in lenguajes:
    print(l)
```

l = primero muestra python, luego C, luego c++ y finalmente java

3. for range

```
for i in range(1, 11):
    print(i)
```