#Atividades 1º Período LPA

# Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500:
soma = 0
for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:
        soma += i

print(soma)
# Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e mostrar:
    #A. Menor Altura;
    #B. Menor Altura;
meh = float('inf')
mah = float('-inf')

for i in range(15):
    altura = float(input(f'Digite aqui a altura da {i+1}ª pessoa: '))
    if altura < meh:
        meh = altura
    if altura > mah:
        mah = altura

print(f'A menor altura do grupo é {meh:.2f} m.')
print(f'A maior altura do grupo é {mah:.2f} m.')

# Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a
    #média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores
       # negativos e o percentual de valores negativos e positivos.
soma = 0
q_positivos = 0
q_negativos = 0

while True:
    valor = float(input('Digite um valor (ou 0 para sair): '))
    if valor <= 0:
        break
    
    soma += valor
    
    if valor > 0:
        q_positivos += 1
    else:
        q_negativos += 1

total_valores = q_positivos + q_negativos
media = soma / total_valores

perc_positivos = q_positivos / total_valores * 100
perc_negativos = q_negativos / total_valores * 100

print(f'A média aritmética dos valores é {media:.2f}.')
print(f'{q_positivos} valores são positivos ({perc_positivos:.2f}% do total).')
print(f'{q_negativos} valores são negativos ({perc_negativos:.2f}% do total).')

# Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles
    #estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve
        #terminar quando for lido um número negativo.
cont_0_25 = 0
cont_26_50 = 0
cont_51_75 = 0
cont_76_100 = 0

while True:
    num = float(input('Digite um número (ou um valor negativo para sair): '))
    if num < 0:
        break
    
    if 0 <= num <= 25:
        cont_0_25 += 1
    elif 26 <= num <= 50:
        cont_26_50 += 1
    elif 51 <= num <= 75:
        cont_51_75 += 1
    elif 76 <= num <= 100:
        cont_76_100 += 1

print(f'{cont_0_25} números estão no intervalo [0-25].')
print(f'{cont_26_50} números estão no intervalo [26-50].')
print(f'{cont_51_75} números estão no intervalo [51-75].')
print(f'{cont_76_100} números estão no intervalo [76-100].')

#  Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200.
    #Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos números lidos. 
    # O número que encerrará a leitura será zero.
numeros = []
numero = int(input('Digite um número: '))
while numero != 0:
    numeros.append(numero)
    numero = int(input('Digite um número: '))

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 == 1]

media_pares = sum(pares) / len(pares) if len(pares) > 0 else 0
media_geral = sum(numeros) / len(numeros) if len(numeros) > 0 else 0

print(f'Números pares: {len(pares)}')
print(f'Números ímpares: {len(impares)}')
print(f'Média dos números pares: {media_pares:.2f}')
print(f'Média geral dos números: {media_geral:.2f}')

#  Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200.
for i in range(101, 200, 2):
    print(i)
    
# Escrever um algoritmo que leia um valor para uma variável N de 1 a 10 e calcule a tabuada de N. Mostre a tabuada na forma: 0 x N = 0, 1 x N = 1N, 2 x N = 2N, ..., 10 x N = 10N.
N = int(input("Digite um número de 1 a 10: "))

while N < 1 or N > 10:
    N = int(input("Valor inválido! Digite um número de 1 a 10: "))

for i in range(11):
    print(f"{i} x {N} = {i*N}")
    
# Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em P.A contendo valores 10 valores.
A = float(input("Digite o valor inicial da P.A.: "))
R = float(input("Digite a razão da P.A.: "))

for i in range(10):
    print(A)
    A += R
    
# Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em P.G contendo 10 valores
A = float(input("Digite o valor inicial da P.G.: "))
R = float(input("Digite a razão da P.G.: "))

for i in range(10):
    print(A)
    A *= R
# Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120
A = int(input("Digite um número inteiro para calcular o seu fatorial, painhooo =   "))

fatorial = 1

print(f"{A}! = ", end="")

for i in range(A, 0, -1):
    fatorial *= i
    print(i, end="")
    if i != 1:
        print(" X ", end="")
    else:
        print(" = ", end="")
        
print(fatorial)


