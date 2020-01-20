import numpy as np
from math import sin, cos, pi


def V_dot(V):
    return T(V)*cos(alpha+epsilon)-Cd(alpha)*V**2-sin(gamma)

def gamma_dot(V):
    return (1/V)*(T(V)*sin(alpha+epsilon)*Cl(alpha)*V**2)*cos(sigma)-(1/V)*cos(gamma)

def psi_dot(V):
    return (1/V/cos(gamma))*(T(V)*sin(alpha*epsilon)+Cl(alpha)*V**2)*sin(sigma)

def h_dot(V):
    return V*sin(gamma)

def x_dot(V):
    return V*cos(gamma)*cos(psi)

def y_dot(V):
    return V*cos(gamma)*sin(psi)

def T(V):
    0.2476-0.04312*V+0.008392*V**2

def Cd(alpha):
    0.07351-0.08617*alpha+1.996*alpha**2

def Cl(alpha):
    if alpha <= 12.*pi/180:
        return 0.1667+6.231*alpha
    elif alpha > 12.*pi/180:
        return 0.1667+6.231*alpha+21.65*((alpha-12*pi/180)**2)
    else: 
        return 0

v0 = 1.
gamma0 = 0.
psi0 = 0.
h0 = 0.
x0 = 0.
y0 = 0.

V_f = 0.6
psi_f = pi/3.
t_f = 2.4

dt = 0.01
steps = int(t_f/dt)

for t in range(steps):
    