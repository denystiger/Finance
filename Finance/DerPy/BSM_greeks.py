import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'serif'
import mpl_toolkits.mplot3d.axes3d as p3

from BSM import d1f, N, dN

def BSM_delta(St, K, t, T, r, sigma):
    ''' Black-Sholes Delta'''
    d1 = d1f(St, K, t, T, r, sigma)
    delta = N(d1)
    return delta
def BSM_gamma(St, K, t, T, r, sigma):
    ''' Black sholes Gamma of european call option'''
    d1 = d1f(St, K, t, T, r, sigma)
    gamma = dN(d1) / (St * sigma * np.sqrt(T - t))
    return gamma
def BSM_theta(St, K, t, T, r, sigma):
    ''' Black sholes Theta of european call option'''
    d1 = d1f(St, K, t, T, r, sigma)
    d2 = d1 -sigma *np.sqrt(T-t)
    theta = (-St * dN(d1) * sigma / (2 * np.sqrt(T - t))
         - r * K * np.exp(-r * (T - t)) * N(d2))
    return theta
def BSM_rho(St, K, t, T, r, sigma):
    ''' Black sholes Rho of european call option'''
    d1 = d1f(St, K, t, T, r, sigma)
    d2 = d1 -sigma *np.sqrt(T-t)
    rho = K * (T-t) * np.exp(-r *(T-t)) * N(d2)
    return rho
def BSM_vega(St, K, t, T, r, sigma):
    ''' Black sholes Vega of european call option'''
    d1 = d1f(St, K, t, T, r, sigma)
    vega = dN(d1) *St  * np.sqrt(T - t)
    return vega

def plot_greeks(function, greek):
    # Model params
    St = 100.0
    t = 0.
    r = 0.05
    sigma = 0.2

    # Strike and maturity ranges
    klist = np.linspace(80, 120, 25)
    tlist = np.linspace(0.01, 1, 25)

    # Value grid
    V = np.zeros((len(tlist), len(klist)), dtype=float)
    for i in range(len(tlist)):
        for j in range(len(klist)):
            V[i, j] = function(St, klist[j], t, tlist[i], r, sigma)

    # Mesh for plotting
    K_grid, T_grid = np.meshgrid(klist, tlist)

    # Plot
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(K_grid, T_grid, V, cmap='viridis')
    ax.set_xlabel('Strike $K$')
    ax.set_ylabel('Maturity $T$')
    ax.set_zlabel('%s(K, T)' % greek)
    ax.set_title('%s Surface' % greek)
    plt.tight_layout()
    plt.show()
