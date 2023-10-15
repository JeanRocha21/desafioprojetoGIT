def calculo (participante, cachorros):
  media = cachorros / participante
  
  return media
# Abaixo segue um exemplo de código que você pode ou não utilizar
#valores = input().split() 

#:  Calcule a média de cachorros quentes consumidas por participante e imprima o valor com DUAS casas decimais.
participante = 11
cachorros = 840

resultado = calculo(participante, cachorros)

print(f'{resultado:.2f}')