# Exercício de fixação 2: Crie um programa que pergunte o nome do cliente para ser inserido em um cartão de crédito,
#  com espaço máximo de 20 caracteres. Caso o usuário informe um nome maior, deve mostrar uma mensagem informando que
# o nome é extenso demais e deve ser abreviado. Dica: para saber o tamanho de uma string, usar a função len. Exemplo: len(nome).

nome = input(
    "Digite o nome do cliente para o cartão de crédito (máximo 20 caracteres): ")
for i in range(len(nome)):
    if i > 19:
        print("O nome é extenso demais e deve ser abreviado.")
        break
