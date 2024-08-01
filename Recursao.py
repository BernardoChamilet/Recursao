def somaDigitosR(n):
    if len(str(n)) == 1:
        return(n)
    else:
        return(int(str(n)[-1]) + somaDigitosR(int(str(n)[0:-1])))

def somaDigitosI(n):
    n = str(n)
    x = len(n)
    soma = 0
    for i in range(0,x):
        soma = soma + int(n[i])
    return(soma)

def somaElementosI(V):
    n = len(V)
    soma = 0
    for i in range(0,n):
        soma = soma + V[i]
    return(soma)
    
def somaElementosR(V):
    if len(V) == 1:
        return(V[0])
    else:
        return(V[-1] + somaElementosR(V[0:-1]))

def fatorialI(n):
    res = 1
    while n > 0:
        res = res * n
        n = n - 1
    return(res)

def fatorialR(n):
    if n == 0:
        return(1)
    else:
        return(n * fatorialR(n-1))
    
def fibI(n):
    if n == 1:
        return(1)
    cont = 0
    soma = 0
    anterior = 1
    anterior2 = 0
    while cont < n-1:
        soma = anterior + anterior2
        cont = cont + 1
        anterior2 = anterior
        anterior = soma
    return(soma)

def fibR(n):
    if n == 0 or n == 1:
        return(n)
    else:
        return(fibR(n-1) + fibR(n-2))

print(somaDigitosR(543))
print(somaDigitosI(543))
print(somaElementosR([5,4,3]))
print(somaElementosI([5,4,3]))
print(fatorialI(4))
print(fatorialR(4))
print(fibI(5))
print(fibR(5))