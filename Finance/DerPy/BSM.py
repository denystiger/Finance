import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.family'] = 'serif'

from scipy.integrate import quad

# Helpers
def dN(x):
    ''' Prob density function of standard normal random variable x '''
    return math.exp(-0.5 * x**2) / math.sqrt(2 * math.pi)

def N(d):
    ''' Cumulative density function '''
    return quad(lambda x: dN(x), -20, d, limit=50)[0]

def d1f(St, K, t, T, r, sigma):
    ''' Black-Scholes d1 function '''
    d1 = (math.log(St / K) + (r + 0.5 * sigma**2) * (T - t)) / (sigma * math.sqrt(T - t))
    return d1

def BSM_call_value(St, K, t, T, r, sigma):
    ''' Calculate Black-Scholes European call option value '''
    d1 = d1f(St, K, t, T, r, sigma)
    d2 = d1 - sigma * math.sqrt(T - t)
    call_value = St * N(d1) - K * math.exp(-r * (T - t)) * N(d2)
    return call_value

def BSM_put_value(St, K, t, T, r, sigma):
    ''' Calculate Black-Scholes European put option value '''
    put_value = BSM_call_value(St, K, t, T, r, sigma) - St + math.exp(-r * (T - t)) * K
    return put_value

# Plotting function
def plot_values(function):
    plt.figure(figsize=(10, 8.3))
    points = 100

    # Model parameters
    St = 100.0
    K = 100.0
    t = 0.
    T = 1.
    r = 0.05
    sigma = 0.2

    # C(K) plot
    plt.subplot(221)
    klist = np.linspace(80, 120, points)
    vlist = [function(St, K_, t, T, r, sigma) for K_ in klist]
    plt.plot(klist, vlist)
    plt.grid(True)
    plt.xlabel('strike $K$')
    plt.ylabel('present value')

    # C(T) plot
    plt.subplot(222)
    tlist = np.linspace(0.0001, 1, points)
    vlist = [function(St, K, t, T_, r, sigma) for T_ in tlist]
    plt.plot(tlist, vlist)
    plt.grid(True)
    plt.xlabel('maturity $T$')

    # C(r) plot
    plt.subplot(223)
    rlist = np.linspace(0., 0.1, points)
    vlist = [function(St, K, t, T, r_, sigma) for r_ in rlist]
    plt.plot(rlist, vlist)
    plt.grid(True)
    plt.xlabel('short rate $r$')
    plt.ylabel('present value')
    plt.axis('tight')

    # Sigma plot
    plt.subplot(224)
    slist = np.linspace(0.01, 0.5, points)
    vlist = [function(St, K, t, T, r, sigma_) for sigma_ in slist]
    plt.plot(slist, vlist)
    plt.grid(True)
    plt.xlabel('volatility $\sigma$')
    plt.tight_layout()
    plt.show()

# Execute plotting function for call value


