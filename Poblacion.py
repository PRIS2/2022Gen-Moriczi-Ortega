#Declaro una lista de individuos
import secrets
import Individuo

poblacion = []
#Declaro una lista de individuos que se van a cruzar y mutar
poblacion_cruza_mutacion = []

#metodo para rellenar la lista poblacion con x individuos
def rellenar_poblacion(x):
    for i in range(x):
        genes = []
        #Creo un nuevo individuo
        individuo = Individuo.individuo(genes)
        individuo.rellenar_genes()
        poblacion.append(individuo)

#creo una funcion para mostrar la poblacion
def mostrar_poblacion(lista_individuos):
    for individuo in lista_individuos:
        print(individuo.genes)

#metodo que devuelve una lista con los individuos cruzados pasando una lista de individuos ademas
# de una probabilidad de mutacion pasada por parametro
def cruzar_mutar_individuos(lista_individuos, probabilidad):
    punto = secrets.randbelow(10)
    lista_cruza_mutacion = []
    if probabilidad < 0.5:
        print("Ha habido mutación en la poblacion ")
    for individuo in lista_individuos:
        random = secrets.randbelow(len(lista_individuos))
        individuo_cruza = individuo.cruzar_punto(lista_individuos[random], punto)
        if probabilidad < 0.5:
            individuo_mutacion = individuo_cruza.mutar(probabilidad)
            lista_cruza_mutacion.append(individuo_mutacion)
        else:
            lista_cruza_mutacion.append(individuo_cruza)
    return lista_cruza_mutacion

#Pruebo el metodo de cruzarMutarIndividuos, generando una poblacion inicial de individuos.
#Luego genero una lista con los individuos cruzados y mutados aleatoriamente
#muestro la poblacion inicial y la poblacion cruzada y mutada
rellenar_poblacion(10)
random = secrets.randbelow(2)

print("Población inicial:")
mostrar_poblacion(poblacion)
print("\n")
poblacion_cruza_mutacion = cruzar_mutar_individuos(poblacion,random)
print("Población cruzada y mutada: ")
mostrar_poblacion(poblacion_cruza_mutacion)