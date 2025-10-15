import sys

try:
    float_Ladoa = float(input('Informe o lado "A" do Triângulo: '))
    float_Ladob = float(input('Informe o lado "B" do Triângulo: '))
    float_Ladoc = float(input('Informe o lado "C" do Triângulo: '))

except ValueError:
    sys.exit('ERRO: Você deve digitar um valor numérico.')

except Exception as strErro:
    sys.exit(f'ERRO: {strErro}')

else:
    if float_Ladoa <= 0 or float_Ladob <= 0 or float_Ladoc <= 0:
        sys.exit('O número informado deve ser maior que "0".')

    if (float_Ladoa + float_Ladob > float_Ladoc and
        float_Ladoa + float_Ladoc > float_Ladob and
        float_Ladob + float_Ladoc > float_Ladoa):
        print('É Triângulo.')
    else:
        print('Não é Triângulo.')