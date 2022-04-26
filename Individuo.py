from array import array
class individuo:
#atributos de cada individuo de la poblacion de la generacion actual

    padre = [1,2,4,6,7,8,0]
    madre = [0,6,4,42,42,4,2]
    hijo = []

    def __init__(self, padre, madre, hijo):
        self.padre = padre
        self.madre = madre
        self.hijo = hijo

    def getPadre(self):
        return self.padre

    def getMadre(self):
        return self.madre

    def getHijo(self):
        return self.hijo

    def setPadre(self, padre):
        self.padre = padre

    def setMadre(self, madre):
        self.madre = madre

    def setHijo(self, hijo):
        self.hijo = hijo

    def __str__(self):
        return "Padre: " + str(self.padre) + " Madre: " + str(self.madre) + " Hijo: " + str(self.hijo)

    def __repr__(self):
        return "Padre: " + str(self.padre) + " Madre: " + str(self.madre) + " Hijo: " + str(self.hijo)  

    def __eq__(self, other):
        return self.padre == other.padre and self.madre == other.madre and self.hijo == other.hijo


#metodo para crear un individuo a partir de un padre y una madre y una posicion de la matriz de genes a mutar 
def crearIndividuo(padre, madre, posicion):
    hijo = []
    for i in range(len(padre)):
        if i == posicion:
            hijo.append(madre[i])
        else:
            hijo.append(padre[i])
    return hijo






print(crearIndividuo(individuo.padre, individuo.madre, 3))