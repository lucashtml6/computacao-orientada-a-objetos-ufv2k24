farinha = int(input('Digite a quantidade de farinha: ')) #2
ovos = int(input('Digite a quantidade de ovos: ')) #3
leite = int(input('Digite a quantidade de leite: ')) #5

qtdBolosFarinha = farinha // 2
qtdBolosOvos = ovos // 3
qtdBolosLeite = leite // 5

bolos = (qtdBolosFarinha * 2 + qtdBolosOvos * 3 + qtdBolosLeite * 5) // 10

print(bolos)
