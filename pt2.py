m = 17

class TablaHash:
    def __init__(self):
        self.tamano = m
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
#print(H.datos)


