import numpy as np
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def edades(n,maxi):
    l = np.random.randint(0,maxi,size=n)
    return l

def intento(intents):
    Gente = []
    for muerte in range(30,100):
        for i in range(intents):
            lo = edades(1000,muerte+1)
            esco = np.random.choice(lo,2)
            if (np.amax(esco)==muerte):
                Gente.append(np.amax(esco))
    a,b,c= plt.hist(Gente, bins=100, density=True)
    ii=np.argmax(a)
    plt.scatter(b[ii],a[ii], s=15, c="r")
    mean = np.mean(a)
    plt.plot(mean)
    plt.show()
    plt.title("Max: " + str(np.amax(a)) + " Promedio: " + str(mean))
    plt.savefig('histogram.pdf')
    return Gente

intento(1000)
