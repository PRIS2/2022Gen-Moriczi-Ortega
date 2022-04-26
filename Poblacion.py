#Declaro una lista de individuos
import random
import Individuo

poblacion = []
#Declaro una lista de individuos que se van a cruzar
poblacionCruzada = []
#Declaro una lista de individuos que se van a mutar
poblacionMutacion = []
#Declaro una lista de individuos que se van a cruzar y mutar
poblacionCruzaMutacion = []



#metodo para rellenar la lista poblacion con x individuos
def rellenarPoblacion(x):
    for i in range(x):
        #Declaro una lista de genes de tamaño 10 con valores entre 0 y 1
        genes = []
        #bucle para rellenar la lista de genes con valores 0 o 1
        for i in range(10): 
            genes.append(random.randint(0,1))
        #Creo un nuevo individuo con los genes de los padres cruzados
        individuo = Individuo.individuo(genes)
        poblacion.append(individuo)

#creo una funcion para mostrar la poblacion
def mostrarPoblacion():
    for individuo in poblacion:
        print(individuo.genes)  

rellenarPoblacion(10)
mostrarPoblacion()

for individuo in poblacion:
    if random.random() < 0.5:
        poblacionCruzada.append(individuo)
    else:
        poblacionMutacion.append(individuo)

#Pendiente de hacer el cruzamiento y mutacion de los individuos de la poblacionCruzada y poblacionMutacion respectivamente a partir de la poblacion 