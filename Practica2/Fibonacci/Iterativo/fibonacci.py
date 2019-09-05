#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 2 Fibonacci Iterativa
def fibonacci ( n ):
    count, fibo, a, b, f = 1, 1, 1, 0, [ ]
    for i in range ( 1, n ):
        count += 1
        fibo = a + b
        count += 1
        f.append ( fibo )
        count += 1
        b = a
        count += 1
        a = fibo
        count += 1
    count += 1
    print("contador: ", count)
    return fibo, count, f