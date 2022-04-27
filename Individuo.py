import secrets
class individuo:

    #Declaro una lista de genes de tamaño 10 con valores entre 0 y 1
    genes = []

    #bucle para rellenar la lista de genes con valores 0 o 1
    # Se hace uso de secret() para generar un numero aleatorio entre 0 y 1
    # ya que segun sonarcloud no se puede usar random.randint por seguridad

    def rellenar_genes(self):
        for i in range(10):
            random = secrets.randbelow(2)
            self.genes.append(random)

    #contructor de la clase individuo que recibe una lista de genes
    def __init__(self, genes):
        self.genes = genes

    #Metodo para cruzar 2 individuos y devolver un nuevo individuo con los genes de los padres cruzados indicando el punto de cruce
    def cruzar_punto(self, individuo2, punto):
        #Declaro una lista de genes de tamaño 10 con valores entre 0 y 1
        genes_cruza = []
        #bucle para rellenar la lista de genes con valores 0 o 1
        #Descoemtar siguiente linea para imprimir el punto de cruce
        # print("Punto de cruce: " + str(punto))
        for i in range(10):
            if i < punto:
                genes_cruza.append(self.genes[i])
            else:
                genes_cruza.append(individuo2.genes[i])
        #Creo un nuevo individuo con los genes de los padres cruzados
        individuo_cruza = individuo(genes_cruza)
        return individuo_cruza

    #Metodo para mutar un individuo y devolver un nuevo individuo con uno de los genes mutados pasando una probabilidad
    def mutar(self, probabilidad):
        #Declaro una lista de genes de tamaño 10 con valores entre 0 y 1
        genes_mutacion = []
        #bucle para rellenar la lista de genes con valores 0 o 1
        for i in range(10):
            random = secrets.randbelow(2)
            if random <= probabilidad:
                #Descoemtar siguiente linea para imprimir el gen mutado
                # print("Gen mutado: " + str(i))
                if self.genes[i] == 0:
                    genes_mutacion.append(1)
                else:
                    genes_mutacion.append(0)
            else:
                genes_mutacion.append(self.genes[i])
        #Creo un nuevo individuo con los genes de los padres cruzados
        individuo_mutacion = individuo(genes_mutacion)
        return individuo_mutacion