# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;
def calculoviagem (tempo, velocidade):
  total = tempo * velocidade
  
  return total

def consumototal (total, consumomedio):
  consumo = total / consumomedio
  
  return consumo

# Abaixo segue um exemplo de código que você pode ou não utilizar
valores = input().split()
tempo = int(valores[0])
velocidade = int(valores[1])

calculodistancia = calculoviagem(tempo, velocidade)
consumomedio = 12
resultado = consumototal(calculodistancia, consumomedio)

print(f'{resultado:.3f}')

# TODO:  Calcule quantidade de litros necessária para realizar a viagem e imprima com TRÊS dígitos após o ponto decimal