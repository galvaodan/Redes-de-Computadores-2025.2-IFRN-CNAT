import sys
valorA = float(input('Digite o valor de A: '))

if valorA == 0:
    sys.exit("Valor de A igual a 0. A equação não será do 2º grau.")

valorB = float(input('Digite o valor de B: '))
valorC = float(input('Digite o valor de C: '))

# verificar se o valode de a é igual a zero, se for sair do programa.

'''Verificar se o valor de a é zero. Caso seja, a equação não será do 
2º grau e o programa deve informar o usuário sobre isso e encerrar;'''

# Calcular o discriminante (delta) e, com base no valor de delta:

floatDelta = (valorB **2) -4 * valorA * valorC

print (f'O valor de delta é igual a: {floatDelta}')

#definido a raiz quadrada de delta

floatRaizdelta = floatDelta**0.5

# Definido X1 e X2

floatX1 = (-valorB + floatRaizdelta) / (2*valorA)
floatX2 = (-valorB - floatRaizdelta) / (2*valorA)


'''- delta > 0 : a equação possui duas raízes reais distintas. 
			  O programa deve calcular e exibir ambas as raízes;'''

if floatDelta >0:
    print(f'A equação possui duas raízes reais distintas são elas: {floatX1} e {floatX2}')

    #delta = 0 : a equação possui uma única raiz real.  O programa deve calcular e exibir a raiz única;

elif floatDelta == 0:
    print(f'A equação possui uma única raíz real distinta: {floatX1} e {floatX2}')

    #delta < 0 : a equação não possui raízes reais. O programa deve informar ao usuário que não existem raízes reais.

else: floatDelta <0
sys.exit("Valor de Delta menor que 0. Não existem raízes reais.")