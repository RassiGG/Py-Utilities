coordenada_x = float(input("Digite a coordenada x"))
coordenada_y = float(input("Digite a coordenada y"))
if coordenada_x >0 and coordenada_y >0:
    print("coordenadas maior que zero")
elif coordenada_x <0 and coordenada_y >0:
    print('Coordenadas menor e maior que zero')
elif coordenada_x <0 and coordenada_y <0:
    print("Coordenadas menores que zero")
elif coordenada_x >0 and coordenada_y <0:
    print("Coordenada x maior e y menor que zero")
else:
    print("O ponto está localizado no eixo")