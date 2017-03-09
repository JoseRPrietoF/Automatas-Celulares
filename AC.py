import matplotlib.pyplot as plt

def AC(inicial,regla,t):
    lista = list()
    lista.append(inicial)
    seed = inicial
    longSeed = len(seed)
    reglaN = BinarizacionDeReglas(regla)
    for i in range(t):
        linea = list()
        for j in range(longSeed):
            aux = list()
            index0 = (j-1) % longSeed
            index1 = j % longSeed
            index2 = (j+1) % longSeed
            aux.append(seed[index0])
            aux.append(seed[index1])
            aux.append(seed[index2])
            aux = buscarRegla(reglaN,aux)
            linea.append(aux)
        lista.append(linea)
        seed = linea

    return lista


def BinarizacionDeReglas(n):
    lista = list()
    regla = list('{0:08b}'.format(n)) # 22
    regla = regla[::-1] # 22 al reves=  01101000
    regla = [int(x) for x in regla]  # a numeros
    for i in range(8):
        num = list('{0:03b}'.format(i))
        num = [int(x) for x in num] # a numeros
        num.append(regla[i])
        lista.append(num)
    return lista

# Cases
def buscarRegla(regla, n):
    if(len(n) != (len(regla[0])-1)):
        print("Error en las longitudes al buscar regla")
        return None
    for i in range(len(regla)):
        if(regla[i][0] == n[0] and regla[i][1] == n[1] and regla[i][2] == n[2]):
            return regla[i][3]
    return None

def plotAc(ac):

    plt.subplot(111)
    plt.imshow(ac, cmap='Greys', interpolation='nearest')
    #plt.savefig('blkwht.png')

    plt.show()



x = BinarizacionDeReglas(22)
print(x)
ac = AC([0,0,1,0,1,1,1,0,0,1,1,1,0,0,1,0,1,0,0,1],169,25)
print(ac)
plotAc(ac)
