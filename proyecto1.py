# Matematica discreta proyecto 1
# AndresEmilioQuinto 18288
# AndreeToledo 18439


#-----------------------------------------------------------------------------------------------------------------

def linearCongruentialMethod(s, m, a, c, randomNums, QTYrandomNums):
    # Inicializamos el estado de semilla
    randomNums[0] = s

    # Cantidad de numeros aleatorios
    for i in range(1, QTYrandomNums):

        # Seguimos el modelo visto en clase de congruencia lineal
        # ref: https://drive.google.com/drive/u/0/folders/1XizWdUQp5X4o4nmjqAJUbbQbpnTk2Koq
        randomNums[i] = ((randomNums[i - 1] * a) + c) % m


# Codigo Main del programa

#-----------------------------------------------------------------------------------------------------------------

mod_ulo = 17
class TablaHash:
    def __init__(self):
        self.tamano = mod_ulo
        self.ranuras = [None] * self.tamano
        self.datos = [None] * self.tamano

    def agregar(self,clave,dato):
      valorHash = self.funcionHash(clave,len(self.ranuras))

      if self.ranuras[valorHash] == None:
        self.ranuras[valorHash] = clave
        self.datos[valorHash] = dato
      else:
        if self.ranuras[valorHash] == clave:
          self.datos[valorHash] = dato  #reemplazo
        else:
          proximaRanura = self.rehash(valorHash,len(self.ranuras))
          while self.ranuras[proximaRanura] != None and \
                          self.ranuras[proximaRanura] != clave:
            proximaRanura = self.rehash(proximaRanura,len(self.ranuras))

          if self.ranuras[proximaRanura] == None:
            self.ranuras[proximaRanura]=clave
            self.datos[proximaRanura]=dato
          else:
            self.datos[proximaRanura] = dato #reemplazo

    def funcionHash(self,clave,tamano):
         return clave%tamano

    def rehash(self,hashViejo,tamano):
        return (hashViejo+1)%tamano

    def obtener(self,clave):
      ranuraInicio = self.funcionHash(clave,len(self.ranuras))

      dato = None
      parar = False
      encontrado = False
      posicion = ranuraInicio
      while self.ranuras[posicion] != None and  \
                           not encontrado and not parar:
         if self.ranuras[posicion] == clave:
           encontrado = True
           dato = self.datos[posicion]
         else:
           posicion=self.rehash(posicion,len(self.ranuras))
           if posicion == ranuraInicio:
               parar = True
      return dato

    def __getitem__(self,clave):
        return self.obtener(clave)

    def __setitem__(self,clave,dato):
        self.agregar(clave,dato)

#-----------------------------------------------------------------------------------------------------------------
menu = input("""
|||||||||||||||||MENU|||||||||||||||||||||
Bienvenido al programa de nuestro proyecto,
porfavor ingrese que funcion desea probar.
Ingrese una opcion por su numeral:
1: Funcion de dispersion
2: Generador de n ́umeros pseudoaleatorios
3: Salir
""")
#-----------------------------------------------------------------------------------------------------------------
if menu == "2":

    print("Ingrese el valor de la semilla s: \n")
    s = int(input())
    print("Ingrese el valor del modulo M: \n")
    m = int(input())
    print("Ingrese el valor de el multiplicador termino a: \n")
    a = int(input())
    print("Ingrese el valor del incremento termino c: \n")
    c = int(input())
    print("HACIENDO CALCULOS....: \n")
    print("El resultado final es: \n")

    #Cantidad de numeros aleatorios a generar
    QTYrandomNums = 20

    # Array donde vamos a almacenar los numeros generados
    randomNums = [0] * (QTYrandomNums)

    # Llamada de la funcion
    linearCongruentialMethod(s, m, a, c, randomNums,QTYrandomNums)

    # Resultado final y print de los resultados
    for i in randomNums:
        print(i, end=" ")

elif menu == "1":
    a = [1489,1237,1312,1548,1209,853,519,992,339,535,883,1246,1325,582,82,1517,744]

    H=TablaHash()
    H[a[0]]="1" 
    a.pop(0)
    H[a[0]]="2"
    a.pop(0)
    H[a[0]]="3"
    a.pop(0)
    H[a[0]]="4"
    a.pop(0)
    H[a[0]]="5"
    a.pop(0)
    H[a[0]]="6"
    a.pop(0)
    H[a[0]]="7"
    a.pop(0)
    H[a[0]]="8"
    a.pop(0)
    H[a[0]]="9"
    a.pop(0)
    H[a[0]]="10"
    a.pop(0)
    H[a[0]]="11"
    a.pop(0)
    H[a[0]]="12"
    a.pop(0)
    H[a[0]]="13"
    a.pop(0)
    H[a[0]]="14"
    a.pop(0)
    H[a[0]]="15"
    a.pop(0)
    H[a[0]]="16"
    a.pop(0)
    H[a[0]]="17"


    print(H.ranuras)
elif menu == "3":
    print("Gracias, feliz dia.")

else:
    ("Ingrese una opcion correcta.")




