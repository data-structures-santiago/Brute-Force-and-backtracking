# 🧠 Ejercicio: Problema de la Mochila (Knapsack Recursivo)

Dado un conjunto de objetos, cada uno con un **nombre**, un **peso** y un **valor**, se desea encontrar la combinación de objetos que **maximice el valor total** sin exceder una capacidad máxima de peso.

Debes implementar una función **recursiva** que explore todas las combinaciones posibles de objetos, imprima cada combinación evaluada (junto con su peso y valor total), y determine cuál es la **mejor combinación posible** bajo la restricción de peso.

### Entrada
- Una lista de objetos representados como tuplas de la forma `(nombre, peso, valor)`.
- Un número entero `W` que representa la **capacidad máxima de la mochila**.

### Salida
- Imprimir todas las combinaciones evaluadas con su peso y valor.
- Mostrar al final:
  - La **mejor combinación** de objetos seleccionados.
  - El **valor total** correspondiente.



# 🧠 Exercise: Recursive Knapsack Problem

## Problem Statement

Given a set of items, each with a **name**, a **weight**, and a **value**, your task is to find the combination of items that **maximizes the total value** without exceeding a given maximum weight capacity.

You must implement a **recursive function** that:
- Explores all possible combinations of including or excluding each item.
- Prints each evaluated combination along with its total weight and value.
- Determines the **best combination** based on the maximum total value that respects the weight constraint.

### Input
- A list of items represented as tuples in the format `(name, weight, value)`.
- An integer `W` representing the **maximum weight capacity** of the knapsack.

### Output
- A printout of all evaluated combinations, showing:
  - The list of item names
  - The total weight
  - The total value
- At the end, print:
  - The **best combination** of selected items.
  - The **maximum total value** obtained.

---


### Ejemplo / Example

#### Entrada / Input

```python
items = [
    ("A", 1, 12),
    ("B", 5, 10),
    ("C", 2, 16),
    ("D", 9, 17),
    ("E", 10, 13)
]
W = 20
```


#### salida / Output


🔍 Mejor combinación: ['A', 'B', 'C', 'D']
💰 Valor total: 55

