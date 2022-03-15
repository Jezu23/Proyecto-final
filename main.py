class Consumibles:
    def __init__(self, nombre, avatar):
        self.nombre=nombre
        self.avatar= avatar
    
    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

class Agua(Consumibles):
    def __init__(self,nombre, precio):
        super().__init__(nombre, avatar)
        self.precio= precio
    
    def getPrecio(self):
        print("El precio del %s es %s$" % (self.nombre, self.precio))
        
class Cocacola(Consumibles):
    def __init__(self,nombre, precio):
        super().__init__(nombre, avatar)
        self.precio=precio
    
    def getPrecio(self):
        print("El precio de la %s es %s$" % (self.nombre, self.precio))

class Fanta(Consumibles):
    def __init__(self,nombre, precio):
        super().__init__(nombre, avatar)
        self.precio=precio
    
    def getPrecio(self):
        print("El precio de la %s es %s$" % (self.nombre, self.precio))

class Bollicao(Consumibles):
    def __init__(self,nombre, precio):
        super().__init__(nombre, avatar)
        self.precio=precio
    
    def getPrecio(self):
        print("El precio del %s es %s$" % (self.nombre, self.precio))

class Cheetos(Consumibles):
    def __init__(self,nombre, precio):
        super().__init__(nombre, avatar)
        self.precio=precio
    
    def getPrecio(self):
        print("El precio del %s es %s$" % (self.nombre, self.precio))

class Pantalla:
    def __init__(self, consumibles, tam_x, tam_y):
        self.consumibles = consumibles
        self.tam_x = tam_x
        self.tam_y = tam_y
        
    def muestraEscanario(self):
        for x in range(self.tam_x):
            for y in range(self.tam_y):
                consumibleMostrado = False
                for consumible in self.consumibles:
                    if consumible.getX() == x and consumible.getY() == y:
                        print(consumible.getAvatar(),  end = '')
                        consumibleMostrado = True
                        continue
                if not personajeConsumible:
                    print("¡", end = '')
            print()



aguaBezoya = Agua("agua Bezoya", "AB", 1)
aguaBezoya.setX(5)
aguaBezoya.setY(7)
aguaLanjaron= Agua("agua Lanjaron", "AL", 1.20)
aguaLanjaron.setX(5)
aaguaLanjaron.setY(6)
cocacolaNormal = Cocacola("cocacola normal","CN",1.50)
cocacolaNormal.setX(5)
cocacolaNormal.setY(5)
fantaNaranja= Fanta("fanta naranja","FN", 1.50)
fantaNaranja.setX(5)
fantaNaranja.setY(4)
fantaLimon= Fanta("fanta limon", "FL", 1.50)
fantaLimon.setX(5)
fantaLimon.setY(3)
bollicao = Bollicao("bollicao", "B", 1)
bollicao.setX(5)
bollicao.setY(2)
cheetosPandilla= Cheetos("Cheetos Pandilla", "CP",0.45)
cheetosPandilla.setX(5)
cheetosPandilla.ssetY(1)

        
 
while True:
    numero = int(input("Introduce un número del 1 al 7: "))
   
    if numero == 1:
        aguaBezoya.getPrecio()
    
    if numero == 2:
        aguaLanjaron.getPrecio()
    
    if numero == 3:
        cocacolaNormal.getPrecio()
    
    if numero == 4:
        fantaNaranja.getPrecio()
    
    if numero == 5:
        fantaLimon.getPrecio()
    
    if numero ==6:
        bollicao.getPrecio()
    
    if numero ==7:
        cheetosPandilla.getPrecio()
        
    continuar=input("¿Desea realizar otra compra?")
    if continuar == "No":
        print("Muchas gracias")
        break
    
    
    