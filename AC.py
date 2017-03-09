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

def plotAcAnimated(ac):
    lista = list()
    plt.ylim(len(ac)-1)
    for x in ac:
        lista.append(x)
        plt.imshow(lista, cmap='gray', interpolation='nearest')
        plt.pause(0.00000001)
    plt.pause(20)

x = BinarizacionDeReglas(22)
print(x)
regla = 169
inicial = [0,0,1,0,1,1,1,0,0,1,1,1,0,0,1,0,1,0,0,1]
inicial2 = [0,0,1,0,1,1,1,0,0,1,1,1,0,0,1,0,1,0,0,1,1,0,0,1,0,1,1,0,1,1,0,0,1,0,1,0,0,0,0,1,0,1,0,1,1,1,0,0,1,1,1,0,0,1,0,1,0,1,1,1,0,0,1,1,1,0,0,1,0,1,0,1,0,1]
ac = AC(inicial2,regla,100)
#plotAc(ac)
print(len(ac))
plotAcAnimated(ac)

