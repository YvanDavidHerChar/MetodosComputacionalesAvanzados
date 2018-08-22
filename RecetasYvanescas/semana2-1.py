import numpy as np
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import trapz

def posterior(s):
    r = len(s)
    Na = s.count('a')
    Nb = r-Na
    x = np.linspace(0,1,1000)
    prior = np.exp(-1*(x-0.5)**2/(2*0.1**2))/np.sqrt(2*np.pi*0.1**2)
    likelihood = (x)**Na*(1-x)**Nb
    posterior = likelihood*prior
    B = trapz(posterior)
    posterior = posterior/B
    maxi = float(terior == max(posterior))][0])
    E = trapz(posterior*x)
    var=np.var(posterior)
    std = np.sqrt(var)
    plt.plot(x,posterior)
    plt.xlabel("x") 
    plt.ylabel("y") 
    plt.title("MaxProb = " + str(maxi) + "  Valor Esperado = " + str(E) + "  Desviacion Estandar = " + str(std))
    plt.savefig("posterior.pdf")
    return posterior, likelihood, prior


post,like,prior = posterior('ababa')