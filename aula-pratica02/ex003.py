n = int(input('Digite o valor: '))

def somaFibonacci(n):
    num = 0
    
    if n == 1:
        num = 1
    elif n == 0:
        num = 0
    else:
        num = somaFibonacci(n - 1) + somaFibonacci(n - 2)
    return num
    
sum = 0

for c in range(n):
    sum += somaFibonacci(c)

print(sum)
