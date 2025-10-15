'''
   Escreva um programa que pede ao usuário para inserir um ano e 
   determina se ele é bissexto ou não. 
   
   Um ano é bissexto se atender a uma das seguintes regras:

      - É divisível por 4, mas não é divisível por 100.

      - É divisível por 400.

      (Por exemplo, 2000 e 2400 são bissextos; 1800, 1900 e 2100 não são). 
      
   O programa deve exibir "O ano [ano] é bissexto." ou 
   "O ano [ano] não é bissexto.". 
   
   Use try...except para validar a entrada.'''

import sys
try:
   int_Ano = int(input('Digite o ano: '))
except ValueError:
   sys.exit('ERRO: Você deve digitar um valor numérico.')

except Exception as strErro:
   sys.exit(f'ERRO: {strErro}')

else:
  
   if int_Ano<=0:
      sys.exit('ERRO: o Ano deve ser maio que zero.')

if  (int_Ano % 4 ==0 and int_Ano % 100 != 0) or (int_Ano % 400 ==0):
   print (' Ano bissexto')

else:
    print ('Ano não bissexto')
