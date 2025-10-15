'''
   Desenvolva um código em Python que solicite ao usuário que informe os 
   comprimentos dos três lados de um triângulo. 
   
   Em seguida, verifique se esses comprimentos podem formar um triângulo. 
   Caso afirmativo, calcule e informe os valores dos ângulos do triângulo e 
   classifique-o quanto aos lados e aos ângulos.

   Instruções:
      - Peça ao usuário para inserir os comprimentos dos três lados do triângulo;
      - Verifique se os comprimentos fornecidos podem formar um triângulo. 
        Caso contrário, informe que não é possível formar um triângulo com esses lados;
      - Se for possível formar um triângulo, calcule os três ângulos do triângulo;
      - Classifique o triângulo quanto aos lados (equilátero, isósceles ou escaleno) 
        e aos ângulos (agudo, obtuso ou retângulo);
      - Exiba a classificação do triângulo quanto aos lados e aos ângulos.

   Observações:
      - Para determinar se os lados fornecidos pelo usuário podem formar um triângulo, 
        é necessário verificar a seguinte condição: A soma de quaisquer dois lados de 
        um triângulo deve ser sempre maior que o terceiro lado;
      - Você pode usar a Lei dos cossenos para calcular os ângulos de um triângulo;
      - Para classificar quanto aos lados, verifique se os três lados são iguais 
        (equilátero), se dois lados são iguais (isósceles) ou se todos os lados são 
        diferentes (escaleno);
      - Para classificar quanto aos ângulos, verifique se um dos ângulos é maior que 
        90 graus (obtuso), se um dos ângulos é igual a 90 graus (retângulo) 
        ou se todos os ângulos são menores que 90 graus (agudo);
      - Considere que os ângulos são expressos em graus.

   Dica: Utilize a biblioteca math.
   https://docs.python.org/3/library/math.html
'''
'''A fórmula geral é \(c^{2}=a^{2}+b^{2}-2ab\cos (\^{C})\), onde \(a\), \(b\) e \(c\) são os lados do triângulo e \(\^{C}\) é o ângulo oposto ao lado \(c\).'''
#a + b > c, a + c > b, b + c >

float_Ladoa = float(input('Informe o lado "A" do Triângulo: '))
float_Ladob = float(input('Informe o lado "B" do Triângulo: '))
float_Ladoc = float(input('Informe o lado "C" do Triângulo: '))

if (float_Ladoa + float_Ladob > float_Ladoc or float_Ladoa + float_Ladoc > float_Ladob  or float_Ladob + float_Ladoc >  float_Ladoa):
    print ('É Triângulo')