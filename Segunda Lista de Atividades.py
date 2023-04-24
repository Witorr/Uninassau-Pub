import math as mh
# Segunda Lista de Atividades LPA
#1038
codigo, quantidade = map(int, input('Insira aqui o que você deseja adquirir 1.Cachorro Quente - 2.X-Salada -  3.X-Bacon - 4.Torrada 5.Refrigerante ').split())

if codigo == 1:
    preco = 4.00
elif codigo == 2:
    preco = 4.50
elif codigo == 3:
    preco = 5.00
elif codigo == 4:
    preco = 2.00
elif codigo == 5:
    preco = 1.50

total = preco * quantidade

print("Total: R$ {:.2f}".format(total))

#1040
#Valores:
n1, n2, n3, n4 = map(float, input('Insira suas notas = ').split())

#Média Ponderada:
mp = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

if mp >= 7.0:
    print(f"Media: {mp:.1f}\nAluno aprovado.")
elif mp < 5.0:
    print(f"Media: {mp:.1f}\nAluno reprovado.")
else:
    print(f"Media: {mp:.1f}\nAluno em exame.")
    exame = float(input())
    nova_media = (mp + exame) / 2
    print(f"Nota do exame: {exame:.1f}")
    if nova_media >= 5.0:
        print(f"Aluno aprovado.\nMedia final: {nova_media:.1f}")
    else:
        print(f"Aluno reprovado.\nMedia final: {nova_media:.1f}")
        
#1041
x, y = map(float, input('Insira X e Y = ').split())

if x == y == 0:
    print("Origem")
elif x == 0:
    print("Eixo Y")
elif y == 0:
    print("Eixo X")
elif x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
else:
    print("Q4")

#1043
# Lê os valores de A, B e C
a, b, c = map(float, input('Insira os valores de A, B e C por favor = ').split())

# Condição de  Verificação se os valores formam um triângulo:
if a + b > c and a + c > b and b + c > a:
    
    # Calcula o perímetro
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
else:
    # Calcula a área do trapézio
    area = (a + b) * c / 2
    print(f"Area = {area:.1f}")
    
#1044
a, b = map(int, input().split())

if a % b == 0 or b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
    
#1048
salario = float(input('Digite aqui o valor do seu salário = '))

if salario <= 400:
    percentual = 15
elif salario <= 800:
    percentual = 12
elif salario <= 1200:
    percentual = 10
elif salario <= 2000:
    percentual = 7
else:
    percentual = 4

reajuste = salario * percentual / 100
novo_salario = salario + reajuste

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")

#1051
salario = float(input('Qual o seu salário? = '))

if salario <= 2000.00:
    print("Isento")
else:
    if salario <= 3000.00:
        imposto = (salario - 2000.00) * 0.08
    elif salario <= 4500.00:
        imposto = (1000.00 * 0.08) + ((salario - 3000.00) * 0.18)
    else:
        imposto = (1000.00 * 0.08) + (1500.00 * 0.18) + ((salario - 4500.00) * 0.28)

    print("R$ {:.2f}".format(imposto))
    
#1059 - Professor creio que essa já estava na lista anterior, mas tá aí dnv
for i in range(2, 101, 2):
    print(i)
    
#1067
#Impressão
X = int(input('Digite aqui seu valor inteiro = '))
#Saída
for i in range(1, X+1, 2):
    print(i)
    
