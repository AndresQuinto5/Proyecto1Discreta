# Matematica discreta proyecto 1
# AndresEmilioQuinto 18288
# AndreeToledo 18439


def linearCongruentialMethod(s, m, a, c, randomNums, QTYrandomNums):
    # Inicializamos el estado de semilla
    randomNums[0] = s

    # Cantidad de numeros aleatorios
    for i in range(1, QTYrandomNums):

        # Seguimos el modelo visto en clase de congruencia lineal
        # ref: https://drive.google.com/drive/u/0/folders/1XizWdUQp5X4o4nmjqAJUbbQbpnTk2Koq
        randomNums[i] = ((randomNums[i - 1] * a) + c) % m

# Codigo Main del programa

if __name__ == '__main__':

    print("Ingrese el valor de la semilla s: \n")
    s = int(input())
    print("Ingrese el valor del modulo M: \n ")
    m = int(input())
    print("Ingrese el valor de el multiplicador termino a: \n ")
    a = int(input())
    print("Ingrese el valor del incremento termino c: \n ")
    c = int(input())
    print("HACIENDO CALCULOS....: \n ")
    print("El resultado final es: \n ")

    # # Valor de la semilla
    # s = 3

    # # Parametro del modulo M
    # m = 11

    # # Multiplicador termino a
    # a = 7

    # # Incremento termino c
    # c = 5

    #Cantidad de numeros aleatorios a generar
    QTYrandomNums = 20

    # Array donde vamos a almacenar los numeros generados
    randomNums = [0] * (QTYrandomNums)

    # Llamada de la funcion
    linearCongruentialMethod(s, m, a, c, randomNums,QTYrandomNums)

    # Resultado final y print de los resultados
    for i in randomNums:
        print(i, end=" ")

