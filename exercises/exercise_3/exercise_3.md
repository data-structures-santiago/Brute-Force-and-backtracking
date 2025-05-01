---

## 1. ✨ Subconjuntos con Suma Objetivo / Subsets with Target Sum

### 📜 **Enunciado** / **Problem Statement**
Dado un arreglo de `n` enteros positivos `A` y un entero positivo `K`, determine cuántos subconjuntos de `A` tienen suma exactamente igual a `K`.

Given an array of `n` positive integers `A` and a positive integer `K`, determine how many subsets of `A` have a sum exactly equal to `K`.

---

### 📥 **Entrada** / **Input**


- La primera línea contiene dos enteros: `n` (el tamaño del arreglo) y `K` (la suma objetivo).
- La segunda línea contiene `n` enteros positivos que representan los elementos del arreglo `A`.

- The first line contains two integers: `n` (the size of the array) and `K` (the target sum).
- The second line contains `n` positive integers representing the elements of the array `A`.

---

### 📤 **Salida** / **Output**



- La primera línea contiene dos enteros: `n` (el tamaño del arreglo) y `K` (la suma objetivo).
- La segunda línea contiene `n` enteros positivos que representan los elementos del arreglo `A`.

- The first line contains two integers: `n` (the size of the array) and `K` (the target sum).
- The second line contains `n` positive integers representing the elements of the array `A`.

---

### 📤 **Salida** / **Output**



- Un entero que indica cuántos subconjuntos tienen una suma igual a `K` o los conjuntos correspondientes.

- An integer indicating how many subsets have a sum equal to `K` or subsets  have a sum equal to `K.

---

### 🧩 **Explicación** / **Explanation**
**Entrada** : A = 4, 5

Los subconjuntos `[2, 3]` y `[1, 4]` tienen una suma igual a `5`. Por lo tanto, la salida es `2`o `[2, 3]`,`[1, 4]`.

The subsets `[2, 3]` and `[1, 4]` have a sum equal to `5`. Therefore, the output is `2` or `[2, 3]`,`[1, 4]`.

---

### 🛠️ **Notas** / **Notes**

Este problema es un ejemplo clásico de fuerza bruta y backtracking, donde se exploran todas las combinaciones posibles de subconjuntos para encontrar aquellos que cumplen con la condición de suma objetivo.

This problem is a classic example of brute force and backtracking, where all possible subset combinations are explored to find those that meet the target sum condition.