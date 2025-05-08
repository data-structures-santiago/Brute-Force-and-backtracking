# ♛ Ejercicio: Problema de las N-Reinas (Backtracking)

## Enunciado (Español)

El problema de las N-Reinas consiste en colocar **N reinas** en un **tablero de ajedrez de N×N** de manera que **ninguna reina ataque a otra**. 

Esto significa que:
- No puede haber dos reinas en la misma fila.
- No puede haber dos reinas en la misma columna.
- No puede haber dos reinas en la misma diagonal.

Debes implementar una **función recursiva** con enfoque de **backtracking** que encuentre **todas las posibles soluciones** válidas para un valor dado de `N`, y que imprima cada una de ellas como una matriz o lista de posiciones.

### Entrada
- Un entero `N` que representa el tamaño del tablero y el número de reinas.

### Salida
- Imprimir todas las soluciones posibles (una por línea o bloque), donde cada solución muestra la ubicación de las reinas.
- También se puede mostrar el número total de soluciones al final.

---



# ♛ Exercise: N-Queens Problem (Backtracking)

## Problem Statement

The N-Queens problem consists of placing **N queens** on an **N×N chessboard** so that **no two queens attack each other**.

This means:
- No two queens can be in the same **row**.
- No two queens can be in the same **column**.
- No two queens can be in the same **diagonal**.

You must implement a **recursive backtracking algorithm** that finds **all valid solutions** for a given board size `N`. Each solution should be printed clearly, showing the position of each queen.

---

## Input

- An integer `N` representing both:
  - The size of the board (N rows and N columns)
  - The number of queens to place

---

## Output

- All valid arrangements of N queens, printed one per block.
- Each solution should show the board with `Q` for queens and `.` for empty squares.
- At the end, display the **total number of solutions** found.

---


## Ejemplo / Example

### Entrada / Input

N = 4

### Salida / Output

Solución 1:
. Q . .
. . . Q
Q . . .
. . Q .

Solución 2:
. . Q .
Q . . .
. . . Q
. Q . .

Total de soluciones: 2
