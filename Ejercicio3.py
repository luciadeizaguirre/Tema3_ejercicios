class Naves():
    def __init__(self, nombre, largo, tripulacion,pasajeros):
        self.nombre=nombre
        self.largo=largo
        self.tripulacion=tripulacion
        self.pasajeros=pasajeros
    def __str__(self):
        return f"La nave creada {self.nombre} mide {self.largo} metros, tiene una tripulación de {self.tripulacion} personas y capacidad de {self.pasajeros} pasajeros"
    def ordenar_ascendente(self):        
        lista=[Naves("Ala-X",10,15,100),Naves("Caza TIE",5,8,60),Naves("Destructor estelar",10,30,200),Naves("Lanzadera imperial",8,9,80),
        Naves("Nave real Nubian",7,12,40),Naves("Nave control de droides",7,10,13),Naves("Halcon Milenario",13,10,200),Naves("Estrella de la muerte",3,5,30),
        Naves("Supremacy",10,5,40),Naves("Speeders",2,1,2),Naves("Sandcrawler",8,10,20)]
        return lista.sort(key=lambda x: x.nombre)
    def ordenar_descendente(self):
        lista=[Naves("Ala-X",10,15,100),Naves("Caza TIE",5,8,60),Naves("Destructor estelar",10,30,200),Naves("Lanzadera imperial",8,9,80),
        Naves("Nave real Nubian",7,12,40),Naves("Nave control de droides",7,10,13),Naves("Halcon Milenario",13,10,200),Naves("Estrella de la muerte",3,5,30),
        Naves("Supremacy",10,5,40),Naves("Speeders",2,1,2),Naves("Sandcrawler",8,10,20)]
        return lista.sort(key=lambda x: x.largo, reverse=True)
    def buscar(lista):
        for i in lista:
            return lista[7],lista[8]
    def pasajeros(self):
        lista=[Naves("Ala-X",10,15,100),Naves("Caza TIE",5,8,60),Naves("Destructor estelar",10,30,200),Naves("Lanzadera imperial",8,9,80),
        Naves("Nave real Nubian",7,12,40),Naves("Nave control de droides",7,10,13),Naves("Halcon Milenario",13,10,200),Naves("Estrella de la muerte",3,5,30),
        Naves("Supremacy",10,5,40),Naves("Speeders",2,1,2),Naves("Sandcrawler",8,10,20)]
        lista_pasajeros=[]
        return lista_pasajeros = [range(lista.sort(key=lambda x:x.pasajeros)[0],lista.sort(key=lambda x:x.pasajeros)[5])]
    def tripulacion(self):
        
         




