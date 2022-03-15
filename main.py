class Agua:
    def __init__(self,nombre, precio):
        self.nombre=nombre
        self.precio=precio
    
    def getPrecio(self):
        print("El precio del %s es %s$" % (self.nombre, self.precio))
        
class Cocacola:
    def __init__(self,nombre, precio):
        self.nombre=nombre
        self.precio=precio
    
    def getPrecio(self):
        print("El precio de la %s es %s$" % (self.nombre, self.precio))

class Fanta:
    def __init__(self,nombre, precio):
        self.nombre=nombre
        self.precio=precio
    
    def getPrecio(self):
        print("El precio de la %s es %s$" % (self.nombre, self.precio))

class Bollicao:
    def __init__(self,nombre, precio):
        self.nombre=nombre
        self.precio=precio
    
    def getPrecio(self):
        print("El precio del %s es %s$" % (self.nombre, self.precio))

class Cheetos:
    def __init__(self,nombre, precio):
        self.nombre=nombre
        self.precio=precio
    
    def getPrecio(self):
        print("El precio del %s es %s$" % (self.nombre, self.precio))


aguaBezoya = Agua("agua Bezoya", 1)
aguaLanjaron= Agua("agua Lanjaron", 1.20)
cocacolaNormal = Cocacola("cocacola normal", 1.50)
fantaNaranja= Fanta("fanta naranja", 1.50)
fantaLimon= Fanta("fanta limon", 1.50)
bollicao = Bollicao("bollicao", 1)
cheetosPandilla= Cheetos("Cheetos Pandilla", 0.45)
        
 
while True:
    numero = int(input("Introduce un número del 1 al 7: "))
   
    if numero == 1:
        print(aguaBezoya.getPrecio())
    
    if numero == 2:
        print(aguaLanjaron.getPrecio())
    
    if numero == 3:
        print(cocacolaNormal.getPrecio())
    
    if numero == 4:
        print(fantaNaranja.getPrecio())
    
    if numero == 5:
        print(fantaLimon.getPrecio())
    
    if numero ==6:
        print(bollicao.getPrecio())
    
    if numero ==7:
        print(cheetosPandilla.getPrecio())
        
    
    
    

