import math as mh 
# Atividades BeeCrowd - LPA
# Primeira Listagem de Exercícios
#1001
a = int(input('Insira seu valor A aqui = '))
b = int(input('Insira seu valor B aqui = '))
x = a + b
print("X = {}".format(x))

#1002
raio = float(input('Insira o Valor do seu Raio = '))

pi = 3.14159
area = pi * (raio ** 2)

print(f"A={area:.4f}")

#1003

A = int(input('Insira seu Valor de A aqui = '))
B = int(input('Insira seu Valorzin de B aqui = '))

SOMA = A + B

print("SOMA =", SOMA)

#1004

a = int(input('Insira seu Valor de A aqui = '))
b = int(input('Insira seu Valorzin de B aqui = '))

prod = a * b

print("PROD =", prod)

#1005

A = float(input('Insira aqui seu valor de A = '))
B = float(input('Insira aqui seu valor de B - '))

media = (A * 3.5 + B * 7.5) / 11

print(f"MEDIA = {media:.5f}")

#1006
# leitura das notas:

a = float(input('Digite aqui sua 1º nota = '))
b = float(input('Digite aqui sua 2º nota = '))
c = float(input('Digite aqui sua 3º nota = '))

# cálculo da média ponderada
media = (a*2 + b*3 + c*5)/10

# exibição do resultado com 1 casa decimal
print("MEDIA = {:.1f}".format(media))

#1007

a, b, c, d = map(int, input('Insira aqui os seus valores = ').split())
diferencas = (a * b - c * d)
print("DIFERENÇA =", diferencas)

#1008

numero = int(input(' Qual o valor correspondente ao funcionário? = '))
horas = int(input('Quantas horas trabalhadas você tem? '))
valor_hora = float(input('Quanto vale sua hora trabalhada? '))

salario = horas * valor_hora

print("NUMBER =", numero)
print("SALARY = $", "{:.2f}".format(salario))

#1009

nome = input('Qual o seu nome? ')
salario_fixo = float(input('Quanto você recebe mensalmente? '))
vendas = float(input('Quanto você lucrou com suas vendas esse mês? = '))

comissao = vendas * 0.15
salario_final = salario_fixo + comissao

print(f"TOTAL = R$ {salario_final:.2f}")

#1010
# leitura dos dados da peça 1
cod_peca1, qtd_peca1, preco_peca1 = input('Valores peça 1 = ').split()
cod_peca1 = int(cod_peca1)
qtd_peca1 = int(qtd_peca1)
preco_peca1 = float(preco_peca1)

# leitura dos dados da peça 2
cod_peca2, qtd_peca2, preco_peca2 = input('Valores peça 2 = ').split()
cod_peca2 = int(cod_peca2)
qtd_peca2 = int(qtd_peca2)
preco_peca2 = float(preco_peca2)

# cálculo do valor total da compra
total = qtd_peca1 * preco_peca1 + qtd_peca2 * preco_peca2

# SAÍDA
print("VALOR A PAGAR: R$ {:.2f}".format(total))

#1011

raio = float(input('Digite aqui o valor do seu raio = '))
pi = 3.14159
volume = (4/3) * pi * raio**3

print("VOLUME = {:.3f}".format(volume))

#1012
# Leitura dos valores de entrada:
a, b, c = map(float, input('Insira aqui seus respectivos valores de entrada A, B e C = ').split())

# Cálculo das áreas:
    #LEMBRETE ------->
        #a) a área do triângulo retângulo que tem A por base e C por altura.
        #b) a área do círculo de raio C. (pi = 3.14159)
        #c) a área do trapézio que tem A e B por bases e C por altura.
        #d) a área do quadrado que tem lado B.
        #e) a área do retângulo que tem lados A e B.
#Cálculo:
triangulo = (a * c) / 2
circulo = mh.pi * (c ** 2)
trapezio = ((a + b) * c) / 2
quadrado = b ** 2
retangulo = a * b

# Impressão dos resultados das Formas:
print("TRIANGULO: {:.3f}".format(triangulo))
print("CIRCULO: {:.3f}".format(circulo))
print("TRAPEZIO: {:.3f}".format(trapezio))
print("QUADRADO: {:.3f}".format(quadrado))
print("RETANGULO: {:.3f}".format(retangulo))

#1013

a, b, c = input('Insira seus Valores para cálculo =  ').split() # Leitura dos Valores como str
a, b, c = int(a), int(b), int(c) # Conversão de str 

maior_ab = (a + b + abs(a - b)) / 2 # Calculo do Maior valor 
maior_abc = (maior_ab + c + abs(maior_ab - c)) / 2 #Calculo do Maior Valor entre o antecessor e o valor de C

print(f"{maior_abc} EH o maior") #Saída

#1014:

# Leitura eos valores de distância e combustível
dist = int(input('Qual a distância que será percorrida? = '))
comb = float(input('Quanto você gastou de Gasolina nesse trajeto? = '))

# Calc o consumo médio
consumo_medio = dist / comb

# Mostra o resultado com 3 casas decimais
print('{:.3f} km/l'.format(consumo_medio))

#1015:
    # LEMBRETE
    # Distancia = SQRT (X2 -X1)**2 + (Y2 - Y1)**2

x1, y1 = map(float, input('Insira seus eixos primários = ').split())
x2, y2 = map(float, input('Insira seus exios secundários = ').split())

distancia = mh.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print('{:.4f}'.format(distancia))
